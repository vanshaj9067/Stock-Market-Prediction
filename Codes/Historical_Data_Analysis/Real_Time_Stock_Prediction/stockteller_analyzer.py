# -*- coding: utf-8 -*-
"""
StockTeller Predictor 📊

This script provides an end-to-end system for stock price prediction and analysis
using real-time stock market data via the Yahoo Finance API (yfinance). It includes
data preprocessing, model training (Linear Regression, Random Forest, and SVR),
future price prediction, performance evaluation, alerts on predicted movements,
and optional export of metrics.

Modules Used:
- yfinance: for fetching stock data
- sklearn: for ML model training and evaluation
- pandas, numpy: for data manipulation
- matplotlib, seaborn: for data visualization
- datetime: for handling future prediction dates

Workflow:
1. Fetch stock data from Yahoo Finance for the last 60 days.
2. Preprocess the data and set up training/testing sets.
3. Train multiple ML models.
4. Predict stock prices for the next 5 days.
5. Evaluate model performance using R², MAE, and RMSE.
6. Optionally export results to CSV/Excel.
7. Alert if rise/drop/stable is expected.
8. Visualize predictions using matplotlib.

Author: Sneha Jha
"""

import yfinance as yf  # Yahoo Finance API for real-time financial data
import pandas as pd  # For data manipulation and handling
import numpy as np  # For numerical operations
from sklearn.linear_model import LinearRegression  # Linear Regression model
from sklearn.ensemble import RandomForestRegressor  # Random Forest model
from sklearn.svm import SVR  # Support Vector Regressor
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error,
)  # Model evaluation metrics
import matplotlib.pyplot as plt  # For plotting results
import seaborn as sns  # Optional: for advanced visualizations
import os  # For file path operations
from datetime import datetime, timedelta  # For handling future dates
from sklearn.model_selection import train_test_split  # For splitting dataset


# 1. Fetch Real-Time Data
def fetch_realtime_data(stock_symbol, period="60d"):
    print(f"\U0001f5d5️ Fetching real-time data for {stock_symbol}...")
    df = yf.download(
        stock_symbol, period=period, interval="1d", progress=False
    )  # Download daily data
    df = df.reset_index()  # Reset index to bring 'Date' as a column
    return df


# 2. Preprocess Data
def preprocess_data(df):
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])  # Ensure 'Date' column is datetime
    df.sort_values("Date", inplace=True)  # Sort by date
    df.dropna(inplace=True)  # Remove missing values

    df["Target"] = df["Close"].shift(
        -1
    )  # Set the next day's closing price as the prediction target
    df.dropna(inplace=True)

    features = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    ]  # Selected features for prediction
    X = df[features].values  # Features as input
    y = df["Target"].values  # Target as output

    # Split data into training and testing sets (80-20 split)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return df, X_train, X_test, y_train, y_test


# 3. Train Multiple Models
def train_models(X_train, y_train):
    # Dictionary of models to train
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "SVR": SVR(kernel="rbf"),
    }

    # Train each model
    for name, model in models.items():
        model.fit(X_train, y_train.ravel())
    return models


# 4. Predict Future Prices
def predict_future_prices(df, models, days_ahead=5):
    # Use the last row of features as the starting input
    last_known = (
        df[["Open", "High", "Low", "Close", "Volume"]].values[-1].reshape(1, -1)
    )

    predictions = {name: [] for name in models}  # Store predictions for each model
    future_dates = []  # Store future dates for plotting

    current_input = last_known.copy()
    for i in range(days_ahead):
        for name, model in models.items():
            predicted = model.predict(current_input)[0]  # Predict next day
            predictions[name].append(predicted)

        # Use predicted close as the next day's OHLC input
        next_day = current_input.flatten()
        next_day[0] = next_day[1] = next_day[2] = next_day[3] = predicted
        current_input = next_day.reshape(1, -1)

        # Generate the next date
        next_date = df["Date"].iloc[-1] + timedelta(days=i + 1)
        future_dates.append(next_date)

    return future_dates, predictions


# 5. Evaluate Models
def evaluate_models(models, X_test, y_test):
    scores = []
    for name, model in models.items():
        y_pred = model.predict(X_test)  # Predict using test set
        r2 = r2_score(y_test, y_pred)  # R² Score
        mae = mean_absolute_error(y_test, y_pred)  # Mean Absolute Error
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # Root Mean Square Error

        # Add scores to the list
        scores.append(
            {
                "Model": name,
                "R2 Score": round(r2, 3),
                "MAE": round(mae, 3),
                "RMSE": round(rmse, 3),
            }
        )

    return pd.DataFrame(scores)


# 6. Export Metrics Table
def export_metrics_table(df_metrics):
    choice = (
        input(
            "\n\U0001f4c2 Do you want to export the model comparison table?\nType 'csv' for CSV, 'excel' for Excel, or 'no' to skip: "
        )
        .strip()
        .lower()
    )

    if choice == "csv":
        filename = (
            input("Enter filename (default: model_metrics.csv): ").strip()
            or "model_metrics.csv"
        )
        if not filename.endswith(".csv"):
            filename += ".csv"
        df_metrics.to_csv(filename, index=False)
        print(f"✅ CSV exported to: {os.path.abspath(filename)}")

    elif choice == "excel":
        filename = (
            input("Enter filename (default: model_metrics.xlsx): ").strip()
            or "model_metrics.xlsx"
        )
        if not filename.endswith(".xlsx"):
            filename += ".xlsx"
        df_metrics.to_excel(filename, index=False)
        print(f"✅ Excel file exported to: {os.path.abspath(filename)}")

    else:
        print("⏭️ Skipped exporting.")


# 7. Alert on Stock Movement
def alert_stock_movement(df, predictions):
    print("\n\U0001f514 Stock Alerts:")
    for model, values in predictions.items():
        change = (
            values[-1] - df["Close"].iloc[-1]
        )  # Compare last prediction to last actual close
        if isinstance(change, np.ndarray):
            change = change.item()

        # Define movement thresholds
        direction = (
            "\U0001f4c8 Rise Expected"
            if change > 1
            else "\U0001f4c9 Drop Expected" if change < -1 else "\U0001f500 Stable"
        )
        print(f"{model}: {direction} ({change:.2f} change)")


# 8. Visualize Predictions
def visualize_predictions(df, future_dates, predictions):
    plt.figure(figsize=(10, 5))
    for model, values in predictions.items():
        plt.plot(future_dates, values, label=model)  # Plot each model’s prediction line

    last_close = df["Close"].iloc[-1]
    if isinstance(last_close, pd.Series):
        last_close = last_close.iloc[0]

    plt.axhline(
        y=last_close, color="gray", linestyle="--", label="Last Close Price"
    )  # Reference line
    plt.title("\U0001f4ca Future Stock Price Predictions")
    plt.xlabel("Date")
    plt.ylabel("Predicted Close Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
