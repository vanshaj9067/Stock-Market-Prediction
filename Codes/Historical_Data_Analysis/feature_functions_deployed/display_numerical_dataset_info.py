# Importing OS module for handling file and directory paths
import os
# Importing Pandas for data manipulation and analysis
import pandas as pd
# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to load dataset based on ticker symbol and display its information
DATASET_DIR = 'Preprocessed_Dataset'

def display_numerical_dataset_info(ticker):
    # Define the dataset file path
    dataset_path = os.path.join(DATASET_DIR, f"Preprocessed_{ticker}_Dataset.csv")

    # Check if file exists
    if not os.path.isfile(dataset_path):
        st.error(f"No dataset found for ticker symbol: {ticker}")
        return

    # Load the dataset with 'date' as the index
    df = pd.read_csv(dataset_path, index_col="date")
    df.index.name = "Date"  # Rename index label to 'Date'

    # Display company information based on the ticker symbol
    company_info = {
        "AAPL": "Apple Inc.",
        "GOOG": "Alphabet Inc. (Google)",
        "AMZN": "Amazon.com Inc.",
        "META": "Meta Platforms",
        "MSFT": "Microsoft Corp.",
        "NFLX": "Netflix Inc.",
        "NVDA": "Nvidia Corp.",
        "TCS": "Tata Consultancy Services",
    }

    # Display company name
    company_name = company_info.get(ticker, "Unknown Company")
    st.write(f"**Company Name:** {company_name}")

    # Show dataset details
    st.write("**Dataset Information:**")
    st.write(f"- **Shape:** {df.shape}")
    st.write(f"- **Date Range:** {df.index[0]} to {df.index[-1]}")

    # Capitalize column names for display
    df.columns = [col.capitalize() for col in df.columns]

    # Display starting stock information (first row) and current stock information (last row)
    st.write("**Starting Stock:**")
    st.write(df.iloc[0])

    st.write("**Current Stock:**")
    st.write(df.iloc[-1])

    # Display the first five rows of the dataset (with 'Date' as the index label)
    st.write("**First Five Rows:**")
    st.dataframe(df.head())
