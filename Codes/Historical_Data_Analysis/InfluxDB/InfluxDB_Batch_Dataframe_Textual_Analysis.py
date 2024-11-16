"""
This script processes a CSV dataset containing preprocessed textual data, applies a trained
Naive Bayes model for classification, and sends the resulting predictions to an InfluxDB instance.

Key Steps:
1. Load a CSV file with textual data and corresponding dates.
2. Apply random timestamps to ensure unique date entries.
3. Use a pre-trained Naive Bayes model to classify the 'cleaned_text' column.
4. Vectorize the text using TF-IDF.
5. Append predictions to the dataset and print counts of target labels.
6. Send the processed data, including 'actual_target' and 'predicted_target', to InfluxDB.

Requirements:
- InfluxDB client library (`influxdb_client`)
- Scikit-learn (`sklearn`)
- Pandas (`pandas`)
- Pickle module for loading pre-trained models
"""

import os
import pandas as pd
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import random
from datetime import timedelta

# To ignore warnings
import warnings

warnings.filterwarnings("ignore")

# InfluxDB credentials and configuration
org = "Chhattisgarh Swami Vivekanand Technical University"
token = "gJyTVqkZEBCr8hcVEsp7sohGgv-wvqUSxJ9kxr3k8ZEthXGdVZ00NKirVo4fnu39ujtkSTTAIYNn6HI-Xx4NJg=="
url = "http://127.0.0.1:8086"
bucket = "stock_price"

# Base directory (this script and the subfolders are in the same parent directory)
base_dir = os.path.dirname(os.path.dirname(__file__))

# File paths for the dataset and model
csv_path = os.path.join(
    base_dir, "Textual_Analysis", "Dataset", "Preprocessed_Text_Dataset.csv"
)
model_path = os.path.join(
    base_dir,
    "Textual_Analysis",
    "Models",
    "Classification",
    "pkl_models",
    "Naive_Bayes_Best_Model.pkl",
)

# Step 1: Read the CSV file
data = pd.read_csv(csv_path)

# Step 2: Filter necessary columns and set 'date' as the index
data["date"] = pd.to_datetime(data["date"])


# Step 3: Add random time to the date column to ensure uniqueness
def add_random_time(row):
    """Adds a random time offset to a date to ensure unique timestamps."""
    random_time = timedelta(
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )
    return row + random_time


# Apply the function to the date column
data["date"] = data["date"].apply(add_random_time)

# Step 4: Set 'date' as the index again after modification
data.set_index("date", inplace=True)

# Step 5: Load the pre-trained model
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Step 6: Vectorize the cleaned text data using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_transformed = vectorizer.fit_transform(data["cleaned_text"]).toarray()

# Step 7: Use the model to predict 'cleaned_text'
data["predicted_target"] = model.predict(X_transformed)

# Step 8: Retain only 'Predicted_target' and 'target_encoded' columns for InfluxDB
data = data[["predicted_target", "target_encoded"]]  # Keep only necessary columns
data.rename(
    columns={"target_encoded": "actual_target"}, inplace=True
)  # Rename for consistency

# Print 'actual_target' and 'Predicted_target' before sending to InfluxDB
print("Actual Target and Predicted Target values:")
print(data[["actual_target", "predicted_target"]])

# Display the count of 0 and 1 in 'actual_target' and 'predicted_target' columns
print("Count of actual_target values (0 and 1):")
print(data["actual_target"].value_counts())

print("Count of predicted_target values (0 and 1):")
print(data["predicted_target"].value_counts())

# Display the shape of the DataFrame
print("Shape of the DataFrame:", data.shape)

print(data.head())

# Step 9: Send the DataFrame to InfluxDB
with InfluxDBClient(url=url, token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

    # Write DataFrame to InfluxDB
    write_api.write(
        bucket=bucket,
        org=org,
        record=data,
        data_frame_measurement_name="textual_analysis",
        data_frame_field_columns=[
            "predicted_target",
            "actual_target",
        ],  # Fields for InfluxDB
    )

print("Data successfully sent to InfluxDB.")
