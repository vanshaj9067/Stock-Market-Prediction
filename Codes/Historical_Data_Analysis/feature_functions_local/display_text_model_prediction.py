# Importing OS module for handling file and directory paths
import os
# Importing Pandas for data manipulation and analysis
import pandas as pd
# Importing Pickle for loading/saving pre-trained machine learning models
import pickle
# Importing Streamlit for building the web-based interactive application framework
import streamlit as st
# Text feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to predict and display the text model prediction

def display_text_model_prediction():
    # File paths for the dataset and model
    csv_path = os.path.join(
        "Textual_Analysis", "Dataset", "Preprocessed_Text_Dataset.csv"
    )
    model_path = os.path.join(
        "Textual_Analysis",
        "Models",
        "Classification",
        "pkl_models",
        "Random_Forest_Best_Model.pkl",
    )

    # Step 1: Load the preprocessed dataset
    try:
        data = pd.read_csv(csv_path)
        st.write("Dataset loaded successfully.")
    except FileNotFoundError:
        st.error("Dataset file not found at the specified path.")
        return

    # Step 2: Load the pre-trained model
    try:
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        # st.write("Model loaded successfully.")
    except FileNotFoundError:
        # st.error("Model file not found at the specified path.")
        return

    # Step 3: Vectorize the cleaned text data using TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000)
    X_transformed = vectorizer.fit_transform(data["cleaned_text"]).toarray()

    # Step 4: Streamlit input for user text
    user_input = st.text_input(
        "Enter the text to predict the stock movement (0: Down, 1: Up):"
    )

    if user_input:
        # Step 5: Transform user input using the same vectorizer
        user_input_transformed = vectorizer.transform([user_input]).toarray()

        # Step 6: Use the model to predict the user input
        prediction = model.predict(user_input_transformed)

        # Step 7: Display prediction
        if prediction[0] == 1:
            st.success("The model predicts: Up (1)")
        else:
            st.error(
                "The model predicts: Down (0)"
            )
