# Importing Streamlit
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pickle

# To show Font Awesome icons
css_example = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"> """


# Function to display information about stock market
def display_stock_market_description():

    # Stock Market Overview Markdown
    stock_market_overview = """
    ## Stock Market Overview

    The stock market is a complex system where investors buy and sell shares of publicly traded companies. Understanding fundamental concepts and terminologies is essential for navigating and analyzing market activities effectively.

    ### 1. **What is the Stock Market?**
    - **Definition**: A platform where investors can buy and sell shares of publicly listed companies.
    - **Components**:
    - **Stock Exchanges**: Physical or electronic venues where trading occurs (e.g., NYSE, NASDAQ, BSE).
    - **Listed Companies**: Businesses that have issued shares to the public through an initial public offering (IPO).
    - **Investors**: Individuals or institutions that purchase shares to gain ownership stakes and potential returns.

    ### 2. **Key Terminologies**

    #### a. **Stock (Share)**
    - **Definition**: A unit of ownership in a company.
    - **Types**:
    - **Common Stock**: Provides voting rights and potential dividends.
    - **Preferred Stock**: Typically no voting rights but has a higher claim on assets and dividends.

    #### b. **Stock Exchange**
    - **Definition**: An organized market where securities are bought and sold.
    - **Examples**:
    - **New York Stock Exchange (NYSE)**
    - **NASDAQ**
    - **Bombay Stock Exchange (BSE)**

    #### c. **Index**
    - **Definition**: A statistical measure representing the performance of a group of stocks.
    - **Examples**:
    - **BSE Sensex (BSESN)**: Tracks 30 major companies on the BSE.
    - **S&P 500**: Tracks 500 large-cap U.S. companies.
    - **NASDAQ Composite**: Includes over 3,000 stocks listed on NASDAQ.

    #### d. **Bid and Ask Price**
    - **Bid Price**: The highest price a buyer is willing to pay for a stock.
    - **Ask Price**: The lowest price a seller is willing to accept for a stock.
    - **Spread**: The difference between the bid and ask prices.

    #### e. **Market Order vs. Limit Order**
    - **Market Order**: An order to buy or sell immediately at the current market price.
    - **Limit Order**: An order to buy or sell at a specific price or better.

    #### f. **Volume**
    - **Definition**: The number of shares traded during a specific period.
    - **Significance**: Indicates the activity level and liquidity of a stock.

    #### g. **Volatility**
    - **Definition**: A measure of how much a stock's price fluctuates over a given period.
    - **Types**:
    - **High Volatility**: Large price swings, indicating higher risk.
    - **Low Volatility**: Smaller price movements, indicating lower risk.

    #### h. **Liquidity**
    - **Definition**: The ease with which a stock can be bought or sold without affecting its price.
    - **High Liquidity**: Stocks can be traded quickly with minimal price impact.
    - **Low Liquidity**: Trades may significantly impact the stock price.

    #### i. **Dividend**
    - **Definition**: A portion of a company's earnings distributed to shareholders.
    - **Types**:
    - **Cash Dividend**: Paid in cash.
    - **Stock Dividend**: Paid in additional shares.

    ### 3. **How the Stock Market Works**

    - **Initial Public Offering (IPO)**:
    - **Definition**: The process by which a private company offers shares to the public for the first time.
    - **Purpose**: To raise capital for expansion, pay off debt, or provide liquidity to existing shareholders.

    - **Secondary Market**:
    - **Definition**: The market where previously issued securities are traded among investors.
    - **Function**: Provides liquidity and enables price discovery.

    - **Trading Mechanism**:
    - **Order Matching**: Buy and sell orders are matched through an exchange's order book.
    - **Execution**: Once matched, the trade is executed, and ownership of the shares is transferred.

    ### 4. **Investment Strategies**

    #### a. **Fundamental Analysis**
    - **Definition**: Evaluating a company's financial health, performance, and intrinsic value.
    - **Components**:
    - **Financial Statements**: Income statement, balance sheet, cash flow statement.
    - **Ratios**: Price-to-earnings (P/E), debt-to-equity, return on equity (ROE).
    - **Qualitative Factors**: Management quality, competitive advantage, industry conditions.

    #### b. **Technical Analysis**
    - **Definition**: Analyzing statistical trends from trading activity, such as price and volume.
    - **Tools**:
    - **Charts**: Line charts, bar charts, candlestick charts.
    - **Indicators**: Moving averages, Relative Strength Index (RSI), MACD.

    #### c. **Quantitative Analysis**
    - **Definition**: Using mathematical and statistical models to evaluate securities.
    - **Approach**:
    - **Algorithmic Trading**: Automated trading based on predefined criteria.
    - **Risk Management Models**: Assessing and mitigating financial risks.

    ### 5. **Risk and Return**

    - **Risk**: The possibility of losing some or all of the invested capital.
    - **Return**: The gain or loss generated by an investment.
    - **Risk-Return Tradeoff**: Higher potential returns typically come with higher risk.

    ### 6. **Regulatory Bodies**

    - **Securities and Exchange Commission (SEC)**: U.S. regulatory body overseeing securities markets.
    - **Securities and Exchange Board of India (SEBI)**: Regulatory authority for securities markets in India.
    - **Role**:
    - **Protecting Investors**: Ensuring transparency and fairness in the markets.
    - **Regulating Exchanges**: Setting rules and guidelines for trading activities.
    - **Preventing Fraud**: Detecting and penalizing fraudulent activities.

    ### 7. **Market Participants**

    - **Retail Investors**: Individual investors buying and selling securities for personal accounts.
    - **Institutional Investors**: Entities like mutual funds, pension funds, and insurance companies managing large portfolios.

    ### 8. **Bull and Bear Markets**: 
    - A **bull market** refers to a phase where stock prices are rising or are expected to rise, signaling optimism and confidence among investors.
    - A **bear market** describes a situation where prices are falling or are expected to fall, reflecting pessimism and caution in the market. Investors typically take long positions during bull markets and short positions during bear markets, depending on their market outlook.
    """

    # Display the overview in Streamlit
    st.markdown(stock_market_overview)


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


# Function to display the company data table with logos and details
def display_company_data_table():
    st.markdown(
        """
    <h4>This are all the datasets that are used in the analysis.</h4>

    <table style="width:100%; border-collapse:collapse;">
        <thead>
            <tr style="border-bottom:1px solid #ddd; text-align:left;">
                <th>Company</th>
                <th>Description</th>
                <th>Data Range</th>
                <th>Dataset Shape</th>
                <th>Starting Stock Date</th>
                <th>Current Stock Date</th>
                <th>Starting Stock Price</th>
                <th>Current Stock Price</th>
            </tr>
        </thead>
        <tbody>
            <!-- Google -->
            <tr>
                <td><img src="https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-suite-everything-you-need-know-about-google-newest-0.png"
                        height="40" /> <br> Alphabet Inc. (Google) [GOOG]</td>
                <td>Specializes in Internet-related services and products, including search engines, online advertising, and
                    cloud computing.</td>
                <td>2014-03-27 : 2024-10-17</td>
                <td>(2659, 5)</td>
                <td>2014-03-27</td>
                <td>2024-10-17</td>
                <td>$27.8542</td>
                <td>$164.51</td>
            </tr>
            <!-- Amazon -->
            <tr>
                <td><img src="https://pngimg.com/uploads/amazon/amazon_PNG5.png" height="40" /> <br> Amazon.com Inc. [AMZN]
                </td>
                <td>Started as an online bookstore, now a leader in e-commerce and cloud computing through AWS.</td>
                <td>1997-05-16 : 2024-10-17</td>
                <td>(6901, 5)</td>
                <td>1997-05-16</td>
                <td>2024-10-17</td>
                <td>$0.0863</td>
                <td>$187.53</td>
            </tr>
            <!-- Apple -->
            <tr>
                <td><img src="https://th.bing.com/th/id/R.0ac491574e7ddb71dc2cab65a8bb501f?rik=5NzURUJ1L37UYg&riu=http%3a%2f%2fpurepng.com%2fpublic%2fuploads%2flarge%2fpurepng.com-apple-logologobrand-logoiconslogos-251519938788qhgdl.png&ehk=kQ%2bTI4imrP%2fg9UWIfehFMJOqAn1A3RQTROHV%2f1ORknk%3d&risl=&pid=ImgRaw&r=0"
                        height="40" /> <br> Apple Inc. [AAPL]</td>
                <td>Renowned for innovative consumer electronics, software, and services, including the iPhone and Mac
                    computers.</td>
                <td>1980-12-12 : 2024-10-17</td>
                <td>(11053, 5)</td>
                <td>1980-12-12</td>
                <td>2024-10-17</td>
                <td>$0.0992</td>
                <td>$232.15</td>
            </tr>
            <!-- Meta Platforms -->
            <tr>
                <td><img src="https://static.vecteezy.com/system/resources/previews/024/273/862/original/meta-logo-transparent-free-png.png"
                        height="40" /> <br> Meta Platforms [META]</td>
                <td>Owner of Facebook, a global leader in social media and digital advertising.</td>
                <td>2012-05-18 : 2024-10-17</td>
                <td>(3124, 5)</td>
                <td>2012-05-18</td>
                <td>2024-10-17</td>
                <td>$38.1174</td>
                <td>$576.93</td>
            </tr>
            <!-- Microsoft -->
            <tr>
                <td><img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" height="40" /> <br>
                    Microsoft Corp. [MSFT]</td>
                <td>A leading developer of software, consumer electronics, and personal computers.</td>
                <td>1986-03-13 : 2024-10-17</td>
                <td>(9728, 5)</td>
                <td>1986-03-13</td>
                <td>2024-10-17</td>
                <td>$0.0603</td>
                <td>$416.72</td>
            </tr>
            <!-- Netflix -->
            <tr>
                <td><img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" height="40" /> <br>
                    Netflix Inc. [NFLX]</td>
                <td>Global streaming entertainment service with a vast library of TV series and films.</td>
                <td>2002-05-23 : 2024-10-17</td>
                <td>(5640, 5)</td>
                <td>2002-05-23</td>
                <td>2024-10-17</td>
                <td>$1.1964</td>
                <td>$687.65</td>
            </tr>
            <!-- Nvidia -->
            <tr>
                <td><img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/235_Nvidia_logo-512.png"
                        height="40" /> <br> Nvidia Corp. [NVDA]</td>
                <td>Specializes in graphics processing units and AI technology.</td>
                <td>1999-01-22 : 2024-10-17</td>
                <td>(6477, 5)</td>
                <td>1999-01-22</td>
                <td>2024-10-17</td>
                <td>$0.0377</td>
                <td>$136.93</td>
            </tr>
            <!-- Tata Consultancy Services (TCS) -->
            <tr>
                <td><img src="https://companieslogo.com/img/orig/TCS.NS-7401f1bd.png?t=1631949260" height="40" /> <br> Tata
                    Consultancy Services [TCS]</td>
                <td>Leading global IT services, consulting, and business solutions provider.</td>
                <td>2013-11-01 : 2024-10-17</td>
                <td>(2758, 5)</td>
                <td>2013-11-01</td>
                <td>2024-10-17</td>
                <td>$543.0</td>
                <td>$11.8</td>
            </tr>
        </tbody>        
    </table>
    """,
        unsafe_allow_html=True,
    )


# Directory containing the preprocessed datasets
DATASET_DIR = "Preprocessed_Dataset"


# Function to load dataset based on ticker symbol and display its information
def display_dataset_info(ticker):
    # Define the dataset file path
    dataset_path = os.path.join(DATASET_DIR, f"Preprocessed_{ticker}_Dataset.csv")

    # Check if file exists
    if not os.path.isfile(dataset_path):
        st.error(f"No dataset found for ticker symbol: {ticker}")
        st.write("Files in Preprocessed_Dataset:", os.listdir(DATASET_DIR))

        return

   # Absolute path check
    st.write("Absolute path of dataset directory:", os.path.abspath(DATASET_DIR))
    
    # Check if directory exists
    if not os.path.exists(DATASET_DIR):
        st.error(f"Directory '{DATASET_DIR}' does not exist.")
    else:
        st.write(f"Files in '{DATASET_DIR}':", os.listdir(DATASET_DIR))

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
    st.write("Files in Preprocessed_Dataset:", os.listdir(DATASET_DIR))


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


# Function to display visualizations for the selected ticker
def display_visualizations(ticker):
    # Define the dataset file path
    dataset_path = os.path.join(DATASET_DIR, f"Preprocessed_{ticker}_Dataset.csv")

    # Check if the dataset file exists
    if not os.path.isfile(dataset_path):
        st.error(f"No dataset found for ticker symbol: {ticker}")
        return

    # Load the dataset
    df = pd.read_csv(dataset_path, index_col="date", parse_dates=True)

    # Calculate Moving Average
    df["Moving Average"] = df["close"].rolling(window=20).mean()

    # Calculate RSI
    delta = df["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    # Create the line graph for Open, High, Low, Close prices
    st.subheader(f"{ticker} Price Visualization")
    price_fig = go.Figure()

    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["open"],
            mode="lines",
            name="Open",
            line=dict(color="#fade2a", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["high"],
            mode="lines",
            name="High",
            line=dict(color="#f2495c", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["low"],
            mode="lines",
            name="Low",
            line=dict(color="#5794f2", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["close"],
            mode="lines",
            name="Close",
            line=dict(color="#73bf69", width=4),
            opacity=0.5,
        )
    )

    price_fig.update_layout(
        title="Stock Price Visualization",
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(price_fig)

    # Bar chart for Volume
    st.subheader(f"{ticker} Volume Visualization")

    volume_fig = go.Figure()

    # Set the pastel orange bar color and white outline color
    volume_fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["volume"],
            marker=dict(
                color="teal",  # Pastel Orange for bars
                line=dict(color="teal", width=1),  # White for outline
            ),
            opacity=1,  # Adjust opacity as needed
        )
    )

    volume_fig.update_layout(
        title="Volume Bar Chart",
        xaxis_title="Date",
        yaxis_title="Volume",
        template="plotly_white",
    )

    st.plotly_chart(volume_fig)

    # Moving Average Plot
    st.subheader(f"{ticker} Moving Average Visualization")
    ma_fig = go.Figure()

    ma_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["close"],
            mode="lines",
            name="Close",
            line=dict(color="#ff7f50", width=2),
        )
    )
    ma_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Moving Average"],
            mode="lines",
            name="20-Day Moving Average",
            line=dict(color="#008080", width=2, dash="dash"),
        )
    )

    ma_fig.update_layout(
        title="Moving Average of Closing Price",
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(ma_fig)

    # RSI Plot
    st.subheader(f"{ticker} RSI Visualization")
    rsi_fig = go.Figure()

    rsi_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["RSI"],
            mode="lines",
            name="RSI",
            line=dict(color="#C71585", width=2),
        )
    )  # Different color for RSI
    rsi_fig.add_hline(
        y=70,
        line_dash="dash",
        line_color="#39FF14",
        annotation_text="Overbought (70)",
        annotation_position="top right",
    )
    rsi_fig.add_hline(
        y=30,
        line_dash="dash",
        line_color="yellow",
        annotation_text="Oversold (30)",
        annotation_position="bottom right",
    )

    rsi_fig.update_layout(
        title="Relative Strength Index (RSI)",
        xaxis_title="Date",
        yaxis_title="RSI",
        yaxis_range=[0, 100],
        template="plotly_white",
    )
    st.plotly_chart(rsi_fig)

    # Display information about each plot
    st.write("### Description of Each Plot:")
    st.write(
        "1. **Price Visualization:** Displays the Open, High, Low, and Close prices over time."
    )
    st.write(
        "2. **Volume Visualization:** Shows the trading volume over time as a bar chart."
    )
    st.write(
        "3. **Moving Average Visualization:** Illustrates the 20-day moving average alongside the closing price to smooth out price fluctuations."
    )
    st.write(
        "4. **RSI Visualization:** The RSI is calculated to identify overbought (>70) and oversold (<30) conditions in the stock."
    )


# Function to display visualizations for the selected ticker, including actual vs. predicted prices
def display_model_visualization(ticker):
    # Define the dataset and model paths
    dataset_path = os.path.join(DATASET_DIR, f"Preprocessed_{ticker}_Dataset.csv")
    model_path = os.path.join("Models", "pkl_models", f"{ticker}_Ensemble_Model.pkl")

    # Check if the dataset file exists
    if not os.path.isfile(dataset_path):
        st.error(f"No dataset found for ticker symbol: {ticker}")
        return

    # Load the dataset
    df = pd.read_csv(dataset_path, index_col="date", parse_dates=True)

    # Load the model if available
    if not os.path.isfile(model_path):
        st.error(f"No model found for ticker symbol: {ticker}")
        return

    with open(model_path, "rb") as file:
        model = pickle.load(file)

    # Predict the closing prices
    df["Predicted Close"] = model.predict(
        df.drop(columns=["close"])
    )  # Relevant features are present

    # Calculate Moving Average
    df["Moving Average"] = df["Predicted Close"].rolling(window=20).mean()

    # Calculate RSI
    delta = df["Predicted Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    # Create the line graph for Actual and Predicted Prices
    st.subheader(f"{ticker} Price Visualization")
    price_fig = go.Figure()

    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Predicted Close"],
            mode="lines",
            name="Predicted Close",
            line=dict(color="green", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["open"],
            mode="lines",
            name="Open",
            line=dict(color="#fade2a", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["high"],
            mode="lines",
            name="High",
            line=dict(color="#f2495c", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["low"],
            mode="lines",
            name="Low",
            line=dict(color="#5794f2", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["close"],
            mode="lines",
            name="Actual Close",
            line=dict(color="#B877D9", width=4),
            opacity=0.5,
        )
    )

    price_fig.update_layout(
        title="Stock Price Visualization",
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(price_fig)

    # Predicted vs. Actual Price Plot
    st.subheader(f"{ticker} Actual vs Predicted Price Visualization")
    prediction_fig = go.Figure()

    prediction_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["close"],
            mode="lines",
            name="Actual Close",
            line=dict(color="green", width=2),
        )
    )
    prediction_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Predicted Close"],
            mode="lines",
            name="Predicted Close",
            line=dict(color="red", width=2, dash="dash"),
        )
    )

    prediction_fig.update_layout(
        title="Actual vs Predicted Closing Price",
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(prediction_fig)

    # Bar chart for Volume
    st.subheader(f"{ticker} Volume Visualization")

    volume_fig = go.Figure()
    volume_fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["volume"],
            marker=dict(
                color="teal",  # Set bar color
                line=dict(color="teal", width=1),  # Outline color
            ),
            opacity=1,
        )
    )

    volume_fig.update_layout(
        title="Volume Bar Chart",
        xaxis_title="Date",
        yaxis_title="Volume",
        template="plotly_white",
    )

    st.plotly_chart(volume_fig)

    # Moving Average Plot
    st.subheader(f"{ticker} Moving Average Visualization")
    ma_fig = go.Figure()

    ma_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Predicted Close"],
            mode="lines",
            name="Predicted Close",
            line=dict(color="#ff7f50", width=2),
        )
    )
    ma_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Moving Average"],
            mode="lines",
            name="20-Day Moving Average",
            line=dict(color="#008080", width=2, dash="dash"),
        )
    )

    ma_fig.update_layout(
        title="Moving Average of Closing Price",
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(ma_fig)

    # RSI Plot
    st.subheader(f"{ticker} RSI Visualization")
    rsi_fig = go.Figure()

    rsi_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["RSI"],
            mode="lines",
            name="RSI",
            line=dict(color="#C71585", width=2),
        )
    )
    rsi_fig.add_hline(
        y=70,
        line_dash="dash",
        line_color="#39FF14",
        annotation_text="Overbought (70)",
        annotation_position="top right",
    )
    rsi_fig.add_hline(
        y=30,
        line_dash="dash",
        line_color="yellow",
        annotation_text="Oversold (30)",
        annotation_position="bottom right",
    )

    rsi_fig.update_layout(
        title="Relative Strength Index (RSI)",
        xaxis_title="Date",
        yaxis_title="RSI",
        yaxis_range=[0, 100],
        template="plotly_white",
    )
    st.plotly_chart(rsi_fig)

    # Display information about each plot
    st.write("### Description of Each Plot:")
    st.write(
        "1. **Price Visualization:** Displays the Open, High, Low, and Actual vs. Predicted Close prices over time."
    )
    st.write(
        "2. **Actual vs Predicted Price Visualization:** Compares the model's predicted closing prices with the actual closing prices."
    )
    st.write(
        "3. **Volume Visualization:** Shows the trading volume over time as a bar chart."
    )
    st.write(
        "4. **Moving Average Visualization:** Illustrates the 20-day moving average alongside the closing price to smooth out price fluctuations."
    )
    st.write(
        "5. **RSI Visualization:** The RSI is calculated to identify overbought (>70) and oversold (<30) conditions in the stock."
    )


# Function to Display Model Performance
def display_model_performance():
    # HTML content
    html_content = """
    <h5>Regression Model Performance Overview</h5>
    <p class="description">This table presents the performance of various regression models for different companies. We have utilized an ensemble model approach to enhance prediction accuracy.</p>

    <table>
        <tr>
            <th>Company</th>
            <th>Linear Regression</th>
            <th>Ridge Regression</th>
            <th>Lasso Regression</th>
            <th>Elastic Net Regression</th>
        </tr>
        <tr>
            <td>Apple (AAPL)</td>
            <td>0.9998629224782566</td>
            <td>0.9998630076573156</td>
            <td>0.9993577928176817</td>
            <td>0.9996487306800625</td>
        </tr>
        <tr>
            <td>Amazon (AMZN)</td>
            <td>0.999084553005321</td>
            <td>0.9961820949085249</td>
            <td>0.9961820949085249</td>
            <td>0.9965084504390407</td>
        </tr>
        <tr>
            <td>Google (GOOG)</td>
            <td>0.9992315300913325</td>
            <td>0.9992317269769614</td>
            <td>0.9973035403402394</td>
            <td>0.9973876081990091</td>
        </tr>
        <tr>
            <td>Microsoft (MSFT)</td>
            <td>0.9992315300913325</td>
            <td>0.9998440164467663</td>
            <td>0.9993642265769165</td>
            <td>0.9994838523467628</td>
        </tr>
        <tr>
            <td>Meta (META)</td>
            <td>0.9992315300913325</td>
            <td>0.9992317269769614</td>
            <td>0.9973035403402394</td>
            <td>0.9973876081990091</td>
        </tr>
        <tr>
            <td>Netflix (NFLX)</td>
            <td>0.9992198305734726</td>
            <td>0.9992198288782033</td>
            <td>0.9971600744221598</td>
            <td>0.9971700356054888</td>
        </tr>
        <tr>
            <td>NVIDIA (NVDA)</td>
            <td>0.9971063606802831</td>
            <td>0.998365397592374</td>
            <td>0.9940339650281499</td>
            <td>0.9972701576306695</td>
        </tr>
        <tr>
            <td>Tata Consultancy Services (TCS)</td>
            <td>0.9979612118835919</td>
            <td>0.9979612934362246</td>
            <td>0.9890586523727406</td>
            <td>0.9891227853737217</td>
        </tr>
    </table>
    """

    # Display the HTML content
    st.markdown(html_content, unsafe_allow_html=True)


# Define the function for displaying the model prediction
def display_model_predicted(ticker, open_price, high, low, volume):
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

    # Display historical and predicted data
    df["Predicted Close"] = model.predict(
        df[["open", "high", "low", "volume"]]
    )  # Ensure correct columns

    # Predicted vs. Actual Price Plot
    st.markdown(
        f"<h5>{ticker} Actual vs Predicted Price Visualization</h5>",
        unsafe_allow_html=True,
    )
    prediction_fig = go.Figure()

    prediction_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["close"],
            mode="lines",
            name="Actual Close",
            line=dict(color="green", width=2),
        )
    )
    prediction_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Predicted Close"],
            mode="lines",
            name="Predicted Close",
            line=dict(color="red", width=2, dash="dash"),
        )
    )

    prediction_fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(prediction_fig)


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
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/InfluxDB%20Database/Numerical%20Analysis%201.png" width="100%" alt="Numerical Analysis Snapshot" title="Numerical Analysis Snapshot" />
            <br><br>
        </div>

        <!-- Section 2: Model Prediction -->
        <h5 style="text-align:center;">2. Model Prediction</h5>
        <div style="font-size:16px; text-align:justify;">
            This section displays the model predictions, comparing predicted and actual values for stock prices, RSI, and moving averages.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/InfluxDB%20Database/Model%20Prediction%201.png" width="100%" alt="Model Prediction Snapshot" title="Model Prediction Snapshot" />
            <br><br>
        </div>

        <!-- Section 3: Textual Analysis -->
        <h5 style="text-align:center;">3. Textual Analysis</h5>
        <div style="font-size:16px; text-align:justify;">
            This section visualizes sentiment analysis from news headlines, including positive, negative, and neutral sentiment scores.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/InfluxDB%20Database/Textual%20Analysis%201.png" width="100%" alt="Textual Analysis Snapshot" title="Textual Analysis Snapshot" />
            <br><br>
        </div>

        <!-- Section 4: Hybrid Model -->
        <h5 style="text-align:center;">4. Hybrid Model</h5>
        <div style="font-size:16px; text-align:justify;">
            The hybrid model combines numerical and textual data to provide a more comprehensive analysis of stock prices.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/InfluxDB%20Database/Hybrid%20Model%201.png" width="100%" alt="Hybrid Model Snapshot" title="Hybrid Model Snapshot" />
        </div>


        """,
        unsafe_allow_html=True,
    )


# Function to display the Grafana Dashboard sections
def display_project_dashboard():

    st.markdown(
        """
        <h3 style="text-align:center;">Project Dashboard Overview</h3>
        <div style="font-size:18px; text-align:center;">
            We are using Grafana for efficient data querying and visualization.
        </div>
        <br>
        <div style="text-align:center;">
        <h4>Grafana Dashboard</h4>
        <p>The Grafana dashboard provides an interactive and dynamic interface for real-time data visualization and analysis.</p>
          <img src="https://creazilla-store.fra1.digitaloceanspaces.com/icons/3253859/grafana-icon-md.png" width="150" title = "Grafana Logo" alt="Grafana Logo" />
         <h4>Dashboard Overview</h4>
         <p> This section displays dashboard snapshots from the project, organized by categories.</p>
         <br>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Section 1: Stock Market and Project Dashboard Overview
    st.markdown(
        """
        <h5 style = "text-align:center">1. Stock Market and Project Dashboard Overview</h5>
        <p>
        This section provides an overview of the stock market, project details, and descriptions of the companies used in the project, 
        including MAANG, Nvidia, Microsoft, and TCS.
        </p>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Dashboard%201.png" width="100%" alt="Stock Market Overview Snapshot 1" title="Stock Market Overview Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Dashboard Panel Dashboard Description and Datasets Information View 1.png" width="100%" alt="Stock Market Overview Snapshot 2" title="Stock Market Overview Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Dashboard Panel Dashboard Description and Datasets Information View 2.png" width="100%" alt="Stock Market Overview Snapshot 3" title="Stock Market Overview Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Dashboard Panel Stock Market View 1.png" width="100%" alt="Stock Market Overview Snapshot 4" title="Stock Market Overview Snapshot 4" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    # Section 2: Numerical Analysis
    st.markdown(
        """
        <h5 style = "text-align:center">2. Numerical Analysis</h5>
        <p>
        This section displays numerical data of the stock market, featuring graphs of open, high, low, and close prices 
        along with volume bar plots, RSI, and moving averages.
        </p>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Numerical%20Analysis%201.png" width="100%" alt="Numerical Analysis Snapshot 1" title="Numerical Analysis Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Numerical%20Analysis%202.png" width="100%" alt="Numerical Analysis Snapshot 2" title="Numerical Analysis Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Numerical%20Analysis%203.png" width="100%" alt="Numerical Analysis Snapshot 3" title="Numerical Analysis Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Numerical%20Analysis%204.png" width="100%" alt="Numerical Analysis Snapshot 4" title="Numerical Analysis Snapshot 4" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    # Section 3: Model Prediction
    st.markdown(
        """
        <h5 style = "text-align:center">3. Model Prediction</h5>
        <p>
        This section highlights model predictions, including individual and comparative graphs of predicted and actual values 
        for stock prices, as well as predicted RSI and moving averages.
        </p>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Model%20Prediction%201.png" width="100%" alt="Model Prediction Snapshot 1" title="Model Prediction Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Model%20Prediction%202.png" width="100%" alt="Model Prediction Snapshot 2" title="Model Prediction Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Model%20Prediction%203.png" width="100%" alt="Model Prediction Snapshot 3" title="Model Prediction Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Model%20Prediction%204.png" width="100%" alt="Model Prediction Snapshot 4" title="Model Prediction Snapshot 4" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    # Section 4: Textual Analysis
    st.markdown(
        """
        <h5 style = "text-align:center">4. Textual Analysis</h5>
        <p>
        This section visualizes sentiment analysis from news headlines, showcasing positive, negative, and neutral sentiment scores.
        </p>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Textual%20Analysis%201.png" width="100%" alt="Textual Analysis Snapshot 1" title="Textual Analysis Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Textual%20Analysis%202.png" width="100%" alt="Textual Analysis Snapshot 2" title="Textual Analysis Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Textual%20Analysis%203.png" width="100%" alt="Textual Analysis Snapshot 3" title="Textual Analysis Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Textual%20Analysis%204.png" width="100%" alt="Textual Analysis Snapshot 4" title="Textual Analysis Snapshot 4" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    # Section 5: Hybrid Model
    st.markdown(
        """
        <h5 style = "text-align:center">5. Hybrid Model</h5>
        <p>
        The hybrid model combines numerical and textual data for a comprehensive analysis.
        </p>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Hybrid%20Model%201.png" width="100%" alt="Hybrid Model Snapshot 1" title="Hybrid Model Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Hybrid%20Model%202.png" width="100%" alt="Hybrid Model Snapshot 2" title="Hybrid Model Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Hybrid%20Model%203.png" width="100%" alt="Hybrid Model Snapshot 3" title="Hybrid Model Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical%20Data%20Analysis/Database_Dashboard_Snapshots/Grafana%20Dashboard/Hybrid%20Model%204.png" width="100%" alt="Hybrid Model Snapshot 4" title="Hybrid Model Snapshot 4" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )


# Function to display team members' contact information in a transposed, column-wise format
def display_contact_information():

    # Define team member information as separate rows with transposed details
    team_members = [
        {
            "Name": "Madhurima Rawat",
            "Role": "Project Planner & Developer",
            "Responsibilities": "Project planning, managing GitHub repository, setting up InfluxDB database, Grafana dashboard design, Streamlit deployment, Flask styling and layout, data visualization and preprocessing of numerical data.",
            "Tools": "GitHub, InfluxDB, Grafana, Streamlit, Flask, Matplotlib, Plotly, Pandas, Python",
            "GitHub": '<a href="https://github.com/madhurimarawat" target="_blank">GitHub</a>',
            "LinkedIn": '<a href="https://www.linkedin.com/in/madhurima-rawat/" target="_blank">LinkedIn</a>',
            "Email": '<a href="mailto:rawtamadhurima@gmail.com" target="_blank">Email</a>',
        },
        {
            "Name": "Geetanshu Dev Meshram",
            "Role": "Data Analyst & Backend Developer",
            "Responsibilities": "Model building for numerical data, basic Flask app design.",
            "Tools": "Python, Flask, Machine Learning libraries",
            "GitHub": '<a href="https://github.com/geetanshudev" target="_blank">GitHub</a>',
            "LinkedIn": '<a href="https://www.linkedin.com/in/geetanshu-dev-meshram-2b3b61240/" target="_blank">LinkedIn</a>',
            "Email": '<a href="mailto:meshramgeetanshudev@gmail.com" target="_blank">Email</a>',
        },
        {
            "Name": "Sneha Jha",
            "Role": "Data Analyst",
            "Responsibilities": "Processing text data, model building, and hybrid model building.",
            "Tools": "NLP libraries, Hybrid Model Building",
            "GitHub": '<a href="https://github.com/Sneha100802" target="_blank">GitHub</a>',
            "LinkedIn": '<a href="https://www.linkedin.com/in/sneha-jha-808796261/" target="_blank">LinkedIn</a>',
            "Email": '<a href="mailto:jhasneha344@gmail.com" target="_blank">Email</a>',
        },
    ]

    # Display a brief summary of the team with names, LinkedIn profiles, and a description
    st.markdown("### Team Overview")
    st.markdown(
        "Our team consists of three passionate individuals who bring diverse skills to the table. "
        "We are focused on developing cutting-edge solutions in data analytics, backend development, and project management. "
        "Each team member plays a critical role in the success of the project, and we are excited to share our expertise and dedication."
    )

    # Explicitly written details for each team member with LinkedIn links
    st.markdown(
        "[Madhurima Rawat](https://www.linkedin.com/in/madhurima-rawat/) : &nbsp; Project Planner & Developer specialized in Project planning, managing GitHub repository, setting up InfluxDB database, Grafana dashboard design, Streamlit deployment, Flask styling and layout, data visualization and preprocessing of numerical data. Tools: GitHub, InfluxDB, Grafana, Streamlit, Flask, Matplotlib, Plotly, Pandas, Python"
    )
    st.markdown(
        "[Geetanshu Dev Meshram](https://www.linkedin.com/in/geetanshu-dev-meshram-2b3b61240/) :  &nbsp; Data Analyst & Backend Developer specialized in Model building for numerical data, basic Flask app design. Tools: Python, Flask, Machine Learning libraries"
    )
    st.markdown(
        "[Sneha Jha](https://www.linkedin.com/in/sneha-jha-808796261/) :  &nbsp; Data Analyst specialized in Processing text data, model building, and hybrid model building. Tools: NLP libraries, Hybrid Model Building"
    )

    st.markdown("---")

    # HTML Table with centered content and reduced width
    html_table = f"""
    <table style="width: 80%; border: 1px solid black; border-collapse: collapse; margin-left: auto; margin-right: auto;">
        <tr>
            <th style="padding: 8px; text-align: center;"><i class="fas fa-id-card"></i> &nbsp; Name</th>
            <th style="padding: 8px; text-align: center;">Madhurima Rawat</th>
            <th style="padding: 8px; text-align: center;">Geetanshu Dev Meshram</th>
            <th style="padding: 8px; text-align: center;">Sneha Jha</th>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-user-tie"></i> &nbsp; <strong>Role</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Role']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Role']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Role']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-tasks"></i> &nbsp; <strong>Responsibilities</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Responsibilities']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Responsibilities']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Responsibilities']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-tools"></i> &nbsp; <strong>Tools</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Tools']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Tools']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Tools']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fab fa-github"></i> &nbsp;<strong>GitHub</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['GitHub']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['GitHub']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['GitHub']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fab fa-linkedin"></i> &nbsp;<strong>LinkedIn</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['LinkedIn']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['LinkedIn']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['LinkedIn']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-envelope"></i> &nbsp;<strong>Email</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Email']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Email']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Email']}</td>
        </tr>
    </table>
    """

    # Render the table
    st.markdown(html_table, unsafe_allow_html=True)


# Main function to handle the selection and display of sections
def main():
    st.title("Stock Market Prediction")

    # Sidebar navigation
    st.sidebar.title("Explore")
    selected_section = st.sidebar.radio(
        "Go to",
        [
            "Stock Market Description",
            "Project Description",
            "Companies",
            "Dataset Information",
            "Dataset Visualization",
            "Model Evaluation",
            "Model Visualization",
            "Model Prediction",
            "InfluxDB Database",
            "Grafana Dashboard",
            "Meet the Team",
        ],
    )

    # Include Font Awesome CSS
    st.sidebar.markdown(
        """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <div class="sidebar-content">
        <h1><a href="https://github.com/madhurimarawat/Stock-Market-Prediction" target="_blank">
                <i class="fab fa-github"></i> &nbsp; Visit Repository
            </a></h1>
    </div>

    """,
        unsafe_allow_html=True,
    )

    # Show sections based on selection
    if selected_section == "Stock Market Description":
        display_stock_market_description()

    elif selected_section == "Project Description":
        display_project_description()

    elif selected_section == "Companies":
        display_company_data_table()

    elif selected_section == "Dataset Information":
        # Dropdown for dataset selection
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )
        # Display dataset information
        display_dataset_info(ticker_symbol)

    elif selected_section == "Dataset Visualization":
        # Dropdown for dataset selection
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )
        # Display dataset information
        display_visualizations(ticker_symbol)

    elif selected_section == "Model Evaluation":

        # Display Model Performance Statistics
        display_model_performance()

    elif selected_section == "Model Visualization":
        # Dropdown for dataset selection
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )
        # Display dataset information
        display_model_visualization(ticker_symbol)

    elif selected_section == "Model Prediction":
        # Dropdown for dataset selection
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )

        # Option to choose between row selection or manual input
        input_method = st.radio(
            "Select Input Method", ("Manual Input", "Select from Dataset")
        )

        if input_method == "Manual Input":
            # Input fields for open, high, low price, and volume
            open_price = st.number_input(
                "Enter Open Price ($)", min_value=0.0, format="%.2f"
            )
            high = st.number_input("Enter High Price ($)", min_value=0.0, format="%.2f")
            low = st.number_input("Enter Low Price ($)", min_value=0.0, format="%.2f")
            volume = st.number_input("Enter Volume", min_value=0, format="%d")

            # Button to trigger prediction
            if st.button("Predict Closing Price"):
                display_model_predicted(ticker_symbol, open_price, high, low, volume)

        else:  # Selecting from the dataset
            # Load the dataset to allow for row selection
            df = pd.read_csv(
                os.path.join(DATASET_DIR, f"Preprocessed_{ticker_symbol}_Dataset.csv"),
                index_col="date",
                parse_dates=True,
            )

            # Dropdown to select a specific row (date)
            date_options = df.index.strftime("%Y-%m-%d").tolist()
            selected_date = st.selectbox("Select Date", date_options)

            # Get values from the selected row
            selected_row = df.loc[selected_date]
            open_price = selected_row["open"]
            high = selected_row["high"]
            low = selected_row["low"]
            volume = selected_row["volume"]

            st.write(f"### Using values for {selected_date}:")
            st.write(
                f"<p>Open Price: <strong>${open_price:.2f}</strong> &nbsp;&nbsp; "
                f"High: <strong>${high:.2f}</strong> &nbsp;&nbsp; "
                f"Low: <strong>${low:.2f}</strong> &nbsp;&nbsp; "
                f"Volume: <strong>{volume}</strong></p>",
                unsafe_allow_html=True,
            )

            # Button to trigger prediction
            if st.button("Predict Closing Price"):
                display_model_predicted(ticker_symbol, open_price, high, low, volume)

    elif selected_section == "InfluxDB Database":
        display_project_database()

    elif selected_section == "Grafana Dashboard":
        display_project_dashboard()

    elif selected_section == "Meet the Team":
        display_contact_information()


# Running the main function
if __name__ == "__main__":
    main()
