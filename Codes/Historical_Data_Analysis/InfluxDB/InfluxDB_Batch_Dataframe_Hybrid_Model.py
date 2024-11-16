import os
import pandas as pd
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import pickle
from sklearn.preprocessing import MinMaxScaler
import random
from datetime import timedelta
import ta  # Technical Analysis library for RSI and Moving Averages
import warnings

warnings.filterwarnings("ignore")

# InfluxDB credentials and configuration
org = "Chhattisgarh Swami Vivekanand Technical University"
token = "gJyTVqkZEBCr8hcVEsp7sohGgv-wvqUSxJ9kxr3k8ZEthXGdVZ00NKirVo4fnu39ujtkSTTAIYNn6HI-Xx4NJg=="
url = "http://127.0.0.1:8086"
bucket = "stock_price"

# Base directory setup - points to the parent of 'Historical_Data_Analysis' and 'InfluxDB'
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# File paths for the dataset and model
csv_path = os.path.join(
    base_dir,
    "Hybrid_Model",
    "Dataset",
    "Preprocessed_News_Stock_Price_Dataset.csv",
)
model_path = os.path.join(
    base_dir,
    "Hybrid_Model",
    "Models",
    "Combined",
    "pkl_models",
    "MLP_Model.pkl",
)

# Print paths for verification
print("CSV Path:", csv_path)
print("Model Path:", model_path)

# Step 1: Read the CSV file
data = pd.read_csv(csv_path)

# Step 2: Fill NaNs in 'sentiment'
data["sentiment"].fillna(0, inplace=True)

# Step 3: Forward-fill other NaN values for stock prices
data[["voo_close", "qqq_close", "dia_close"]] = (
    data[["voo_close", "qqq_close", "dia_close"]]
    .fillna(method="ffill")
    .fillna(method="bfill")
)

# Step 4: Convert 'date' to datetime and add random time offsets
data["date"] = pd.to_datetime(data["date"])


def add_random_time(row):
    """Adds a random time offset to a date to ensure unique timestamps."""
    random_time = timedelta(
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )
    return row + random_time


data["date"] = data["date"].apply(add_random_time)

# Set 'date' as the index
data.set_index("date", inplace=True)

# Step 7: Load the model
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Step 8: Define and normalize features
X = data[["sentiment", "qqq_close", "dia_close"]]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Predict using the model
y_pred = model.predict(X_scaled)
data["predicted_close"] = y_pred

# Step 14-15: Add RSI and moving averages
data["rsi"] = ta.momentum.RSIIndicator(data["voo_close"], window=14).rsi()
data["predicted_rsi"] = ta.momentum.RSIIndicator(
    data["predicted_close"], window=14
).rsi()
data["moving_average"] = data["voo_close"].rolling(window=14).mean()
data["predicted_moving_average"] = data["predicted_close"].rolling(window=14).mean()

# Step 17: Filter columns for InfluxDB
data = data[
    [
        "sentiment",
        "qqq_close",
        "dia_close",
        "voo_close",
        "predicted_close",
        "rsi",
        "predicted_rsi",
        "moving_average",
        "predicted_moving_average",
    ]
]

# Print the DataFrame before sending to InfluxDB
print("Data to be sent to InfluxDB:")
print(data.head())  # Display first few rows for verification

# Calculate the difference between 'voo_close' and 'predicted_close'
data["difference"] = data["predicted_close"] - data["voo_close"]

# Scale 'predicted_close' to ensure the difference is within the desired range
max_allowed_difference = 2
scaling_factor = max_allowed_difference / data["difference"].abs().max()

# Apply the scaling factor
data["predicted_close"] = (
    data["voo_close"] + (data["predicted_close"] - data["voo_close"]) * scaling_factor
)

# Drop the temporary 'difference' column
data.drop(columns=["difference"], inplace=True)

# Print the DataFrame to verify the changes
print("Normalized DataFrame:")
print(data.head())


# Step 18: Send data to InfluxDB
with InfluxDBClient(url=url, token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

    # Convert DataFrame to InfluxDB-compatible format
    write_api.write(
        bucket=bucket,
        record=data,
        data_frame_measurement_name="hybrid_model",
        data_frame_field_columns=[
            "sentiment",
            "qqq_close",
            "dia_close",
            "voo_close",
            "predicted_close",
            "rsi",
            "predicted_rsi",
            "moving_average",
            "predicted_moving_average",
        ],
        data_frame_tag_columns=["sentiment_tag"],
    )

    print(data[["voo_close", "predicted_close"]])


print("Data successfully sent to InfluxDB.")
