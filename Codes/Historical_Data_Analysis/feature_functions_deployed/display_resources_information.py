# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to display resources information

def display_resources_information():
    st.markdown("### Resources and Links")

    # Partial stock prices section
    st.markdown(
        """
        **Partial Stock Prices YAHOO Link:**
        - [Yahoo Finance](https://finance.yahoo.com/)

        **Textual and Hybrid Data:**
        - [Kaggle Dataset - News & Stock Prices](https://www.kaggle.com/datasets/kianso/news-stock-price)
        
        **Complete Stock Price Histories:**
        - [Alphabet/GOOG Stock](https://www.macrotrends.net/stocks/charts/GOOG/google/stock-price-history)
        - [AAPL Stock](https://www.macrotrends.net/stocks/charts/AAPL/apple/stock-price-history)
        - [AMZN Stock](https://www.macrotrends.net/stocks/charts/TCS/container-store/stock-price-history)
        - [META Stock](https://www.macrotrends.net/stocks/charts/META/meta-platforms/stock-price-history)
        - [MSFT Stock](https://www.macrotrends.net/stocks/charts/MSFT/microsoft/stock-price-history)
        - [NFLX Stock](https://www.macrotrends.net/stocks/charts/NFLX/netflix/stock-price-history)
        - [NVDA Stock](https://www.macrotrends.net/stocks/charts/NVDA/nvidia/stock-price-history)
        - [TCS Stock](https://www.macrotrends.net/stocks/charts/TCS/container-store/stock-price-history)

         **Illustration Links:**
        - [Project Resources (Illustration 1)](https://img.freepik.com/premium-vector/flat-design-stock-market-analysis_23-2148590818.jpg)
        - [Streamlit App Background Image (Illustration 2)](https://vectormine.b-cdn.net/wp-content/uploads/Stock_Market.jpg)
        """
    )
