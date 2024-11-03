import os
import pandas as pd
import influxdb_client
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB credentials and configuration
org = "Organization Name"
token = "Token"
url = "http://127.0.0.1:8086"
bucket = "Bucket Name"

# Initialize the InfluxDB client and write API
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Ticker symbols for each dataset
ticker_mapping = {
    # "Alphabet/Google": "GOOG",
    "Apple": "AAPL",
    "Amazon": "AMZN",
    "Meta Platforms": "META",
    "Microsoft": "MSFT",
    "Netflix": "NFLX",
    "Nvidia": "NVDA",
    "Tata Consultancy Services (TCS)": "TCS",
}

# Directory containing the preprocessed dataset files
dataset_dir = os.path.abspath("Preprocessed Dataset")  # Convert to absolute path

# Print all files in the directory to verify access
print("Files in directory:", os.listdir(dataset_dir))

# Loop to process a single dataset file for testing
for company, ticker in ticker_mapping.items():
    # Define the file path
    file_path = os.path.join(dataset_dir, f"Preprocessed_{ticker}_Dataset.csv")
    print(f"Looking for file at: {file_path}")  # Debugging print statement

    # Check if the file exists before proceeding
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}. Skipping {ticker}.")
        continue  # Skip to the next ticker if file not found

    # Read the CSV into a DataFrame
    df = pd.read_csv(file_path, parse_dates=["date"], index_col="date")

    # Add a temporary Ticker column for debugging
    df["Ticker"] = ticker  # Add a Ticker column to the DataFrame

    # Print the DataFrame for debugging
    print(f"DataFrame for {ticker}:")
    print(df)

    # Prepare a list for batch writing
    points = []

    # Convert data to InfluxDB format and prepare for batch write
    for index, row in df.iterrows():
        # Create a data point with Ticker as a tag
        data_point = (
            Point("stock_price").time(index).tag("Ticker", ticker)
        )  # Add Ticker as a tag

        # Add each metric as a field
        for col_name, value in row.items():
            if col_name != "Ticker":  # Skip the Ticker column when writing fields
                data_point.field(col_name, value)  # Use column name as the field

        points.append(data_point)  # Collect data points for batch writing

    # Write all data points to InfluxDB at once
    if points:
        write_api.write(bucket=bucket, org=org, record=points)
        print(f"Written {len(points)} data points for {ticker}.")

print("Data upload process completed.")
