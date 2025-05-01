# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to Display Project Description

def display_project_description():
    st.markdown(
        """
     <h3>Project Description</h3>
    <p>This project aims to analyze and visualize the trends in the stock market using historical financial data. The data is retrieved from Yahoo Finance and analyzed using Python libraries like Pandas and Matplotlib. The visualizations include line graphs, candlestick charts, and scatter plots to showcase the trends in stock prices and volumes.</p>

    <img src="https://img.freepik.com/premium-vector/flat-design-stock-market-analysis_23-2148590818.jpg" style="width: 100%;">
    
    <br>
    <br>
    <h3>Project Overview</h3>

    <p>Our project aims to forecast stock prices by combining numerical data and textual analysis. We utilize historical stock data and insights from financial news to create a robust prediction model.</p>

    <h4>Methodology</h4>

    <ol>
        <li><strong>Data Collection</strong>: We gather historical stock prices of major companies and store them in an InfluxDB database for efficient time-series analysis.</li>
        <li><strong>Data Visualization</strong>: We use Grafana to create dashboards that visualize stock prices and forecast outcomes in real-time.</li>
        <li><strong>Textual Analysis</strong>: Using Natural Language Processing (NLP) tools like NLTK and spaCy, we analyze financial news to gain insights that enhance our predictions.</li>
        <li><strong>Machine Learning</strong>: We are experimenting with advanced models such as ARIMA, LSTM, and Transformers, integrating both numerical and textual data to improve forecasting accuracy.</li>
        <li><strong>Collaboration</strong>: The project is managed through GitHub, allowing our team to collaborate effectively and keep track of changes.</li>
    </ol>

    <h3>Tools Used</h3>

    <ul>
        <li><strong>InfluxDB</strong>: A time-series database for managing stock data.</li>
        <li><strong>Grafana</strong>: A visualization tool for creating dashboards.</li>
        <li><strong>NLP Libraries</strong>: NLTK and spaCy for textual analysis.</li>
        <li><strong>Machine Learning Models</strong>: ARIMA, LSTM, and Transformers for stock price prediction.</li>
    </ul>

    """,
        unsafe_allow_html=True,
    )
