# Importing OS module for handling file and directory paths
import os
# Importing Pandas for data manipulation and analysis
import pandas as pd
# Importing Pickle for loading/saving pre-trained machine learning models
import pickle
# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Define the function for displaying the model prediction
DATASET_DIR = 'Preprocessed_Dataset'

def display_numerical_model_predicted(ticker, open_price, high, low, volume):
    # Define dataset and model paths
    dataset_path = os.path.join(DATASET_DIR, f"Preprocessed_{ticker}_Dataset.csv")
    model_path = os.path.join("Models", "pkl_models", f"{ticker}_Ensemble_Model.pkl")

    # Check if the dataset file exists
    if not os.path.isfile(dataset_path):
        st.error(f"No dataset found for ticker symbol: {ticker}")
        return

    # Load the dataset
    df = pd.read_csv(dataset_path, index_col="date", parse_dates=True)

    # Check if the model file exists
    if not os.path.isfile(model_path):
        st.error(f"No model found for ticker symbol: {ticker}")
        return

    # Load the model
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    # Create a new DataFrame for the input values to predict
    input_data = pd.DataFrame(
        {"open": [open_price], "high": [high], "low": [low], "volume": [volume]}
    )

    # Predict the closing price for the given input values
    predicted_close = model.predict(input_data)[
        0
    ]  # Take the first (and only) prediction

    # Display the prediction
    st.write(f"### Predicted Closing Price for {ticker}: ${predicted_close:.2f}")
