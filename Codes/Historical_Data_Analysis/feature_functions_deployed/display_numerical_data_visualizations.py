# Importing OS module for handling file and directory paths
import os
# Importing Pandas for data manipulation and analysis
import pandas as pd
# Importing Plotly for creating interactive and dynamic visual plots
import plotly.graph_objects as go
# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to display visualizations for the selected ticker
DATASET_DIR = 'Codes/Historical_Data_Analysis/Preprocessed_Dataset'

def display_numerical_data_visualizations(ticker):
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
