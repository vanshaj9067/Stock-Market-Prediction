# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to Display PowerBI Dashboard Plots


def display_power_bi_dashboard():
    st.markdown("### Power BI Dashboard Plots")

    # List of static image URLs from your GitHub repository
    image_urls = [
        "https://raw.githubusercontent.com/madhurimarawat/Stock-Market-Prediction/main/Codes/Historical_Data_Analysis/PowerBI_Dashboard/static/Plots/Amazon_Plot.png",
        "https://raw.githubusercontent.com/madhurimarawat/Stock-Market-Prediction/main/Codes/Historical_Data_Analysis/PowerBI_Dashboard/static/Plots/Apple_Plot.png",
        "https://raw.githubusercontent.com/madhurimarawat/Stock-Market-Prediction/main/Codes/Historical_Data_Analysis/PowerBI_Dashboard/static/Plots/Google_Plot.png",
        "https://raw.githubusercontent.com/madhurimarawat/Stock-Market-Prediction/main/Codes/Historical_Data_Analysis/PowerBI_Dashboard/static/Plots/Meta_Plot.png",
        "https://raw.githubusercontent.com/madhurimarawat/Stock-Market-Prediction/main/Codes/Historical_Data_Analysis/PowerBI_Dashboard/static/Plots/Microsoft_Plot.png",
    ]

    for url in image_urls:
        st.image(url)
