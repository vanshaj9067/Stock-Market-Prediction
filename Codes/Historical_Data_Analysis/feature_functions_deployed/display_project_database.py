# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to display the InfluxDB Database section

def display_project_database():
    st.markdown(
        """
        <h3 style="text-align:center;">Project Database Overview</h3>
        <div style="font-size:18px; text-align:center;">
            We are using InfluxDB Database for efficient data storage and management.
        </div>
        <br>
        <h4 style="text-align:center;">InfluxDB Database</h4>
        <div style="font-size:16px; text-align:justify;">
            InfluxDB is a powerful time-series database optimized for storing and querying both historical and real-time data, 
            particularly in high-volume environments. It offers exceptional performance for managing time-stamped data, making it 
            an ideal choice for our project.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://dashboard.snapcraft.io/site_media/appmedia/2020/07/influxdata-logo--symbol--pool-alpha-small_eSQhzYC.png"
                width="150" title = "InfluxDB Logo" alt="InfluxDB Logo" />
            <br><br>
        </div>
        <h4 style="text-align:center;">InfluxDB Architecture</h4>
        <div style="font-size:16px; text-align:justify;">
            The InfluxDB architecture utilizes a bucket system, which is pivotal for organizing data. In our project, we have a 
            primary bucket named <b>Stock Price</b>. Within this bucket, measurements help categorize and store data efficiently. 
            The first measurement is <b>stock_price</b>, which includes data points such as open, high, low, close, RSI (Relative 
            Strength Index), volume, and moving average, all indexed by time.
            <br><br>
            Another key measurement is <b>model_prediction</b>, containing values such as predicted high, low, open, volume, 
            predicted close, predicted moving average, and predicted RSI.
            <br><br>
            Both measurements include a <b>Ticker</b> column that holds the company ticker symbol, covering a total of eight 
            companies: AAPL, AMZN, MSFT, NVDA, NFLX, META, TCS, and GOOG.
            <br><br>
            Initially, data is stored in InfluxDB, then queried and visualized using Grafana. The dashboard in Grafana is built on 
            top of this architecture, allowing dynamic data visualization. The diagram below depicts the general architecture of 
            InfluxDB.
            <br><br>
        </div>
        
        <div style="text-align:center;">
            <img src="https://wiki.onosproject.org/download/attachments/8423670/influxdb_arch.png?version=1&modificationDate=1459547041415&api=v2"
                width="400" title="InfluxDB Architecture" alt="InfluxDB Architecture" />
        </div>
        <br><br>
        
        <div style="text-align:center;">
            <h4> Database Overview</h4>
            <p> This section displays database snapshots from the project, organized by categories.</p>
        </div>
        <br>

        <!-- Section 1: Numerical Analysis -->
        <h5 style="text-align:center;">1. Numerical Analysis</h5>
        <div style="font-size:16px; text-align:justify;">
            This section displays numerical data from the stock market, including graphs for open, high, low, and close prices. It also features volume bar plots, RSI, and moving averages.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Numerical_Analysis_1.png" width="100%" alt="Numerical Analysis Snapshot" title="Numerical Analysis Snapshot" />
            <br><br>
        </div>

        <!-- Section 2: Model Prediction -->
        <h5 style="text-align:center;">2. Model Prediction</h5>
        <div style="font-size:16px; text-align:justify;">
            This section displays the model predictions, comparing predicted and actual values for stock prices, RSI, and moving averages.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Model_Prediction_1.png" width="100%" alt="Model Prediction Snapshot" title="Model Prediction Snapshot" />
            <br><br>
        </div>

        <!-- Section 3: Textual Analysis -->
        <h5 style="text-align:center;">3. Textual Analysis</h5>
        <div style="font-size:16px; text-align:justify;">
            This section visualizes sentiment analysis from news headlines, including positive, negative, and neutral sentiment scores.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Textual_Analysis_1.png" width="100%" alt="Textual Analysis Snapshot" title="Textual Analysis Snapshot" />
            <br><br>
        </div>

        <!-- Section 4: Hybrid Model -->
        <h5 style="text-align:center;">4. Hybrid Model</h5>
        <div style="font-size:16px; text-align:justify;">
            The hybrid model combines numerical and textual data to provide a more comprehensive analysis of stock prices.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Hybrid_Model_1.png" width="100%" alt="Hybrid Model Snapshot" title="Hybrid Model Snapshot" />
        </div>


        """,
        unsafe_allow_html=True,
    )
