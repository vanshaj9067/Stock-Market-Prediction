# -*- coding: utf-8 -*-
"""
run_analyzer.py

📈 StockTeller Runner Script

This script serves as the main entry point for executing the StockTeller Analyzer pipeline.
It enables stock market enthusiasts and analysts to fetch real-time stock data, preprocess it,
train multiple machine learning models (Linear Regression, Random Forest, SVR), evaluate their
performance, and forecast future stock prices.

Features:
- Real-time stock data fetching via Yahoo Finance (yfinance)
- Data cleaning and preprocessing
- Training and evaluation of multiple predictive models
- Exporting performance metrics and cleaned data
- Future price prediction and visualization
- Alerts based on expected stock movement trends

Usage:
    python run_analyzer.py [TICKER] [DAYS_AHEAD]
    Example:
        python run_analyzer.py AAPL 7
If no arguments are passed, the script defaults to AAPL for the next 5 days.

Author: Sneha Jha
"""

import sys
import yfinance as yf
import pandas as pd
import warnings
import matplotlib.pyplot as plt

# Suppress warnings to keep output clean
warnings.filterwarnings("ignore", category=UserWarning)

# Import functions from the analyzer module
from stockteller_analyzer import (
    fetch_realtime_data,
    preprocess_data,
    train_models,
    evaluate_models,
    predict_future_prices,
    visualize_predictions,
    alert_stock_movement,
    export_metrics_table,
)


def main(ticker=None, days=None):
    # Allow the script to run both via CLI or interactively (e.g., inside a notebook)
    if ticker is None or days is None:
        if len(sys.argv) >= 3:
            ticker = sys.argv[1]  # Get ticker symbol from command-line argument
            days = int(sys.argv[2])  # Get number of days for prediction
        else:
            # Default test values
            ticker = "AAPL"
            days = 5
            print("⚠️ No arguments provided. Running in test mode with default values.")

    # Step 1: Fetch stock data
    print(f"\U0001f4e5 Fetching real-time data for {ticker}...")
    df = fetch_realtime_data(ticker)

    # Step 2: Clean and prepare the dataset
    df_cleaned, X_train, X_test, y_train, y_test = preprocess_data(df)

    # Step 3: Train multiple models on the training set
    trained_models = train_models(X_train, y_train)

    # Step 4: Evaluate the trained models using test data
    print("\n\U0001f4ca Model Comparison:")
    metrics_df = evaluate_models(trained_models, X_test, y_test)
    print(metrics_df)

    # Step 5: Export evaluation metrics (CSV/Excel/Skip)
    export_metrics_table(metrics_df)

    # Step 6: Ask user if they want to export cleaned stock data
    print("\n📊 Do you want to export the cleaned stock data?")
    data_choice = (
        input("Type 'csv' for CSV, 'excel' for Excel, or 'no' to skip: ")
        .strip()
        .lower()
    )

    # Export cleaned data if requested
    if data_choice in ["csv", "excel"]:
        filename_data = input(
            "Enter filename for cleaned data (default: cleaned_data.csv): "
        ).strip()
        if not filename_data:
            filename_data = (
                f"{ticker}_cleaned_data.csv"
                if data_choice == "csv"
                else f"{ticker}_cleaned_data.xlsx"
            )

        try:
            if data_choice == "csv":
                df_cleaned.to_csv(filename_data, index=False)
            else:
                df_cleaned.to_excel(filename_data, index=False)

            print(f"✅ Cleaned data exported to: {filename_data}")
        except Exception as e:
            print(f"❌ Failed to export cleaned data: {e}")
    else:
        print("🚫 Skipped exporting cleaned data.")

    # Step 7: Predict stock prices for specified future days
    future_days, predictions = predict_future_prices(
        df_cleaned, trained_models, days_ahead=days
    )

    # Step 8: Display prediction results as a graph
    visualize_predictions(df_cleaned, future_days, predictions)

    # Pause for a short time and then close all plots to avoid blocking
    plt.pause(2)
    plt.close("all")

    # Step 9: Provide alerts based on forecasted stock movement
    alert_stock_movement(df_cleaned, predictions)

    print("\n✅ Analysis complete. Exiting now.")


# Run main only if script is executed directly (not imported as a module)
if __name__ == "__main__":
    main()
