# Importing OS module for handling file and directory paths
import os

# Importing Pandas for data manipulation and analysis
import pandas as pd

# Importing Pickle for loading/saving pre-trained machine learning models
import pickle

# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Importing TextBlob for basic natural language processing tasks
from textblob import TextBlob

# Function to predict and display the stock price based on user input


def display_hybrid_model_prediction():
    # File path for the pre-trained model
    model_path = os.path.join(
        "Codes",
        "Historical_Data_Analysis",
        "Hybrid_Model",
        "Models",
        "Combined",
        "pkl_models",
        "MLP_Model.pkl",
    )

    # Step 1: Load the pre-trained model
    try:
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        st.write("Model loaded successfully.")
    except FileNotFoundError:
        st.error("Model file not found at the specified path.")
        return

    # Step 2: Streamlit inputs for user data
    dia_close = st.number_input(
        "Enter the DIA close value:", min_value=0.0, format="%.2f"
    )
    qqq_close = st.number_input(
        "Enter the QQQ close value:", min_value=0.0, format="%.2f"
    )
    user_input_text = st.text_input(
        "Enter the news text to calculate sentiment and predict stock price:"
    )

    if user_input_text:
        # Step 3: Calculate sentiment score of the input text
        sentiment_score = TextBlob(user_input_text).sentiment.polarity
        st.write(f"Calculated sentiment score: {sentiment_score:.2f}")

        # Step 4: Combine all inputs into a single DataFrame for model prediction
        final_input = pd.DataFrame(
            {
                "DIA_Close": [dia_close],
                "QQQ_Close": [qqq_close],
                "Sentiment_Score": [sentiment_score],
            }
        )

        # Step 5: Predict using the model
        predicted_price = model.predict(final_input)[0]

        # Step 6: Display prediction with $ symbol
        st.success(f"The model predicts the stock price: ${predicted_price:.2f}")
