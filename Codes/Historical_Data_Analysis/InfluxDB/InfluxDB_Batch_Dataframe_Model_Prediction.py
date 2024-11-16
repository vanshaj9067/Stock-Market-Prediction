"""
This script processes preprocessed stock price datasets and corresponding prediction models for various companies.
It loads each dataset and model, calculates additional technical indicators (RSI and Moving Average) based on the 
predicted close price, and uploads the predicted data (including predicted close prices, RSI, and Moving Average) 
to an InfluxDB database using the DataFrame API for efficient batch processing. The Ticker symbol is added as a tag, 
enabling organized querying in InfluxDB.

Modules Required:
- os: for directory and file path operations
- pandas: for data manipulation and analysis
- influxdb_client: for connecting and writing data to InfluxDB
- pickle: for loading pre-trained models

InfluxDB Configuration:
- org: Organization name for InfluxDB authentication
- token: Access token for InfluxDB
- url: URL for the InfluxDB instance
- bucket: Target InfluxDB bucket for data storage

Technical Indicators:
- RSI (Relative Strength Index): Measures the speed and change of price movements based on the predicted close price.
- Moving Average: Simple moving average of the predicted close price over a specified period.
"""

# Importing Required Libraries
import os
import pandas as pd
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import pickle

# InfluxDB credentials and configuration
org = "Chhattisgarh Swami Vivekanand Technical University"
token = "gJyTVqkZEBCr8hcVEsp7sohGgv-wvqUSxJ9kxr3k8ZEthXGdVZ00NKirVo4fnu39ujtkSTTAIYNn6HI-Xx4NJg=="
url = "http://127.0.0.1:8086"
bucket = "stock_price"

# Initialize the InfluxDB client and write API
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Ticker symbols for each dataset
ticker_mapping = {
    "Apple": "AAPL",
    "Amazon": "AMZN",
    "Alphabet": "GOOG",
    "Meta Platforms": "META",
    "Microsoft": "MSFT",
    "Netflix": "NFLX",
    "Nvidia": "NVDA",
    "Tata Consultancy Services (TCS)": "TCS",
}

# Base directory (this script is located within a subfolder of the project)
base_dir = os.path.dirname(os.path.dirname(__file__))

# Directories for datasets and models using base_dir
dataset_dir = os.path.join(base_dir, "Preprocessed_Dataset")
model_dir = os.path.join(base_dir, "Models", "pkl_models")

# Print all files in the dataset and model directories to verify access
print("Files in dataset directory:", os.listdir(dataset_dir))
print("Files in model directory:", os.listdir(model_dir))


# Function to calculate RSI
def calculate_rsi(data, window=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


# Loop to process each dataset file and its corresponding model
for company, ticker in ticker_mapping.items():
    # Define file paths for dataset and model
    file_path = os.path.join(dataset_dir, f"Preprocessed_{ticker}_Dataset.csv")
    model_path = os.path.join(model_dir, f"{ticker}_Ensemble_Model.pkl")

    print(f"Looking for dataset at: {file_path}")
    print(f"Looking for model at: {model_path}")

    # Check if dataset and model files exist before proceeding
    if not os.path.isfile(file_path):
        print(f"Dataset not found: {file_path}. Skipping {ticker}.")
        continue
    if not os.path.isfile(model_path):
        print(f"Model not found: {model_path}. Skipping {ticker}.")
        continue

    # Read the CSV into a DataFrame
    df = pd.read_csv(file_path, parse_dates=["date"], index_col="date")

    # Load the model
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)

    # The input features (X) are all columns except "close"
    X = df.drop(columns=["close"])

    # Predict the 'close' price using the model
    y_pred = model.predict(X)
    df["predicted_close"] = y_pred  # Add predictions to DataFrame

    # Calculate Moving Average and RSI for the predicted close price
    df["predicted_moving_average"] = df["predicted_close"].rolling(window=20).mean()
    df["predicted_rsi"] = calculate_rsi(df["predicted_close"])

    # Select columns for InfluxDB, including the newly requested columns
    df_influx = df[
        [
            "open",
            "high",
            "low",
            "volume",
            "predicted_close",
            "predicted_moving_average",
            "predicted_rsi",
        ]
    ].copy()
    df_influx.loc[:, "Ticker"] = ticker  # Add Ticker as a tag

    # Write the DataFrame to InfluxDB
    write_api.write(
        bucket=bucket,
        org=org,
        record=df_influx,
        data_frame_measurement_name="model_prediction",
        data_frame_tag_columns=["Ticker"],
    )

    print(f"Written predicted data points for {ticker}.")

print("Model prediction upload process completed.")
