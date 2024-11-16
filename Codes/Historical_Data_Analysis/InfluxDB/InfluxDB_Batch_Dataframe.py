"""
This script reads preprocessed stock price data from CSV files, calculates additional technical indicators (RSI and Moving Average),
and uploads the data to an InfluxDB database in a batch process using Pandas DataFrame. The script iterates through a specified 
directory of CSV files for different companies, reads each file, calculates the RSI and Moving Average, and writes the data to 
InfluxDB with the Ticker symbol as a tag.

### Why Use InfluxDB’s DataFrame Write Mode
Using `InfluxDBClient.write_api().write` with Pandas DataFrame enables efficient batch uploads of time-series data. This approach 
is beneficial when dealing with structured data over regular intervals, as in stock prices, where each record contains a timestamp 
(indexed date) and relevant measurements (closing price, RSI, etc.). Batch uploading allows us to minimize API calls, improving 
performance and reliability when handling large datasets.

### Modules Required
- **os**: for directory and file path operations
- **pandas**: for data manipulation and analysis
- **influxdb_client**: for connecting and writing data to InfluxDB

### InfluxDB Configuration
- **org**: Organization name for InfluxDB authentication
- **token**: Access token for InfluxDB
- **url**: URL for the InfluxDB instance
- **bucket**: Target InfluxDB bucket for data storage

Technical Indicators:
- RSI (Relative Strength Index): Measures the speed and change of price movements based on the predicted close price.
- Moving Average: Simple moving average of the predicted close price over a specified period.

"""

# Importing Required Libraries
import os
import pandas as pd
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

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
    "Meta Platforms": "META",
    "Google": "GOOG",
    "Microsoft": "MSFT",
    "Netflix": "NFLX",
    "Nvidia": "NVDA",
    "Tata Consultancy Services (TCS)": "TCS",
}

# Base directory (assumes this script and related folders are in the same parent directory)
base_dir = os.path.dirname(os.path.dirname(__file__))

# Directory containing the preprocessed dataset files using base_dir
dataset_dir = os.path.join(base_dir, "Preprocessed_Dataset")


# Function to calculate RSI
def calculate_rsi(data, window=14):
    delta = data["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


# Loop to process each dataset file
for company, ticker in ticker_mapping.items():
    file_path = os.path.join(dataset_dir, f"Preprocessed_{ticker}_Dataset.csv")
    print(f"Looking for file at: {file_path}")

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}. Skipping {ticker}.")
        continue

    df = pd.read_csv(file_path, parse_dates=["date"], index_col="date")
    df["Ticker"] = ticker

    # Add Moving Average and RSI columns
    df["moving_average"] = (
        df["close"].rolling(window=20).mean()
    )  # 20-day moving average
    df["rsi"] = calculate_rsi(df)  # RSI calculation

    print(f"DataFrame for {ticker} with added indicators:")
    print(df.head())  # Display the first few rows for verification

    # Write the DataFrame to InfluxDB in batch
    write_api.write(
        bucket=bucket,
        org=org,
        record=df,
        data_frame_measurement_name="stock_price",
        data_frame_tag_columns=["Ticker"],
    )
    print(f"Data for {ticker} written to InfluxDB successfully.")

print("Data upload process completed.")
