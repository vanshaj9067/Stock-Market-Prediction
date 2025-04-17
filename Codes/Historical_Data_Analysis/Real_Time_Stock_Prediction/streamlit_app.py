# -*- coding: utf-8 -*-
"""
stockteller_analyzer

📘 Description:
This Streamlit-based Python app allows users to analyze and forecast stock prices using multiple machine learning models
including Linear Regression, Random Forest, SVM, and LSTM. It also evaluates model accuracy and exports results.

👩‍💻 Authors:
- Sneha Jha: Core logic, model implementations, prediction logic, and visualization.
- Madhurima Rawat: File download and export, date formatting, and comprehensive documentation and comments.

"""

# --- IMPORT LIBRARIES ---

import yfinance as yf  # For fetching historical stock data from Yahoo Finance
import numpy as np  # For numerical operations and arrays
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For plotting and visualizing predictions
import seaborn as sns  # For prettier visualizations (not used directly here)
import torch  # PyTorch for deep learning (LSTM model)
import torch.nn as nn  # For defining neural network layers
from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    precision_score,
    recall_score,
    f1_score,
)  # Model evaluation metrics
from sklearn.linear_model import LinearRegression  # Linear Regression model
from sklearn.ensemble import RandomForestRegressor  # Random Forest Regressor
from sklearn.svm import SVR  # Support Vector Machine Regressor
from sklearn.preprocessing import MinMaxScaler  # For scaling data to a 0–1 range
from datetime import datetime, timedelta  # For handling date/time
import webbrowser  # To open a browser tab for news
import openpyxl  # Required for writing Excel files
import streamlit as st  # Streamlit for creating the web application


# --- CLASS DEFINITION STARTS ---


class StockPricePredictor:
    # Initialize the predictor with ticker name, forecast length, and optional start/end dates
    def __init__(self, ticker, forecast_days, start_date=None, end_date=None):
        self.ticker = ticker  # Stock symbol, e.g., "AAPL" or "TCS.BO"
        self.forecast_days = forecast_days  # Number of future days to predict
        self.start_date = start_date  # Optional user-defined start date
        self.end_date = end_date  # Optional user-defined end date
        self.data = None  # To hold historical stock data
        self.scaler = MinMaxScaler()  # Scaler to normalize stock prices
        self.models = {}  # Dictionary to store trained models
        self.predictions = {}  # Dictionary to store predictions from each model
        self.metrics = pd.DataFrame()  # DataFrame to store evaluation metrics

    def fetch_data(self):
        # Define end date as now if not provided
        end_date = self.end_date or datetime.now()
        # Define start date as 60 days before end if not provided
        start_date = self.start_date or (end_date - timedelta(days=60))
        # If start and end date are same, subtract 5 days to avoid empty range
        if start_date >= end_date:
            start_date = end_date - timedelta(days=5)
        # Add 1 day to include the end date in range
        end_date += timedelta(days=1)

        # Download data from Yahoo Finance using yfinance
        self.data = yf.download(self.ticker, start=start_date, end=end_date)
        # Keep only the 'Close' price and drop missing values
        self.data = self.data[["Close"]].dropna()

        # Store formatted dates for display and file naming
        self.start_date_final = start_date
        self.end_date_final = end_date - timedelta(days=1 - (self.forecast_days - 1))

    def preprocess_data(self):
        # Normalize 'Close' price column
        self.data["Scaled"] = self.scaler.fit_transform(self.data[["Close"]])
        self.X, self.y = [], []  # Initialize input-output data containers

        # Create sliding window sequences for time series
        for i in range(len(self.data) - self.forecast_days):
            # Input = sequence of 'forecast_days'
            self.X.append(self.data["Scaled"].values[i : i + self.forecast_days])
            # Output = next value after the sequence
            self.y.append(self.data["Scaled"].values[i + self.forecast_days])

        self.X = np.array(self.X)  # Convert input to numpy array
        self.y = np.array(self.y)  # Convert output to numpy array

    def train_models(self):
        # Split data for model training
        X_train, y_train = self.X, self.y

        # --- Train Linear Regression model ---
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        self.models["Linear Regression"] = lr

        # --- Train Random Forest Regressor ---
        rf = RandomForestRegressor(n_estimators=100)
        rf.fit(X_train, y_train)
        self.models["Random Forest"] = rf

        # --- Train Support Vector Machine Regressor ---
        svr = SVR(kernel="rbf")
        svr.fit(X_train, y_train)
        self.models["SVM"] = svr

        # --- Define and train LSTM model using PyTorch ---
        class LSTMModel(nn.Module):
            def __init__(self):
                super().__init__()  # Call superclass constructor
                self.lstm = nn.LSTM(
                    input_size=1, hidden_size=50, batch_first=True
                )  # LSTM layer
                self.fc = nn.Linear(50, 1)  # Output layer

            def forward(self, x):
                out, _ = self.lstm(x)  # Forward pass through LSTM
                return self.fc(out[:, -1, :])  # Return last time step's output

        # Prepare LSTM-compatible inputs
        X_train_lstm = torch.tensor(
            X_train.reshape(-1, self.forecast_days, 1), dtype=torch.float32
        )
        y_train_lstm = torch.tensor(y_train.reshape(-1, 1), dtype=torch.float32)

        # Instantiate LSTM model
        lstm = LSTMModel()
        criterion = nn.MSELoss()  # Loss function
        optimizer = torch.optim.Adam(lstm.parameters(), lr=0.01)  # Optimizer

        # Train LSTM for 100 epochs
        for epoch in range(100):
            lstm.train()  # Set model to training mode
            output = lstm(X_train_lstm)  # Get predictions
            loss = criterion(output, y_train_lstm)  # Calculate loss
            optimizer.zero_grad()  # Clear gradients
            loss.backward()  # Backpropagation
            optimizer.step()  # Update weights

        # Save trained LSTM model
        self.models["LSTM"] = lstm

    def predict_future(self):
        # Take last available sequence to forecast future prices
        last_sequence = self.data["Scaled"].values[-self.forecast_days :]

        # Loop through each model to predict
        for name, model in self.models.items():
            future_preds = []  # Store predictions
            input_seq = last_sequence.copy()  # Working input sequence

            # Predict next value, update sequence, repeat
            for _ in range(self.forecast_days):
                X_future = np.array([input_seq])  # Reshape input

                if name == "LSTM":
                    model.eval()
                    with torch.no_grad():
                        input_tensor = torch.tensor(
                            X_future.reshape(-1, self.forecast_days, 1),
                            dtype=torch.float32,
                        )
                        pred = model(input_tensor).numpy().flatten()[0]
                else:
                    pred = model.predict(X_future)[0]

                future_preds.append(pred)  # Save prediction
                input_seq = np.append(input_seq[1:], pred)  # Update input sequence

            # Inverse scale predictions to get actual price
            scaled_preds = self.scaler.inverse_transform(
                np.array(future_preds).reshape(-1, 1)
            ).flatten()
            self.predictions[name] = scaled_preds  # Store results

    def evaluate_models(self):
        # Evaluate all models using multiple metrics
        rows = []  # Store metric rows

        for name, model in self.models.items():
            if name == "LSTM":
                input_tensor = torch.tensor(
                    self.X.reshape(-1, self.forecast_days, 1), dtype=torch.float32
                )
                y_pred = model(input_tensor).detach().numpy().flatten()
            else:
                y_pred = model.predict(self.X)

            y_true = self.y

            # Convert back from scaled values
            if name == "LSTM":
                y_pred = self.scaler.inverse_transform(y_pred.reshape(-1, 1)).flatten()
                y_true = self.scaler.inverse_transform(y_true.reshape(-1, 1)).flatten()

            mse = mean_squared_error(y_true, y_pred)
            r2 = r2_score(y_true, y_pred)
            y_bin = (y_true > np.mean(y_true)).astype(int)  # Convert to binary classes
            y_pred_bin = (y_pred > np.mean(y_pred)).astype(int)
            prec = precision_score(y_bin, y_pred_bin)
            rec = recall_score(y_bin, y_pred_bin)
            f1 = f1_score(y_bin, y_pred_bin)

            rows.append([name, mse, r2, prec, rec, f1])  # Save all metrics

        self.metrics = pd.DataFrame(
            rows, columns=["Model", "MSE", "R2", "Precision", "Recall", "F1"]
        )  # Convert to DataFrame

    def visualize(self):
        # Plot future predictions from all models
        plt.figure(figsize=(12, 6))  # Create figure
        x_range = range(len(self.data), len(self.data) + self.forecast_days)  # X-axis

        for name, pred in self.predictions.items():
            if len(pred) != self.forecast_days:
                st.warning(f"⚠️ Skipping {name} due to shape mismatch in predictions.")
                continue
            plt.plot(x_range, pred, label=name)  # Plot model prediction

        plt.title(f"Predicted Stock Prices for {self.ticker}")
        plt.xlabel("Days Ahead")
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        st.pyplot(plt.gcf())  # Display in Streamlit

    def save_data_csv(self):
        # Save predictions to CSV and provide download button
        if self.predictions:
            start_date = self.data.index[-1] + timedelta(days=1)
            date_range = pd.date_range(
                start=start_date, periods=self.forecast_days, freq="B"
            )  # Business days

            df_output = pd.DataFrame(
                {"Date": date_range.strftime("%Y-%m-%d")}
            )  # Create DataFrame
            df_output["Ticker"] = self.ticker.upper()

            # Add model predictions
            for model_name, values in self.predictions.items():
                if len(values) == len(date_range):
                    df_output[model_name] = [round(price, 4) for price in values]
                else:
                    st.warning(
                        f"Model '{model_name}' returned {len(values)} predictions, expected {len(date_range)}."
                    )

            # Format filename
            start_str = self.start_date_final.strftime("%d-%m-%y")
            end_str = self.end_date_final.strftime("%d-%m-%y")

            csv = df_output.to_csv(index=False).encode("utf-8")  # Convert to CSV
            st.download_button(
                label="📥 Download Forecasted Data as CSV",
                data=csv,
                file_name=f"{self.ticker}_Predictions__{start_str}_to_{end_str}.csv",
                mime="text/csv",
            )

    def export_results(self):
        # Export metrics and predictions to Excel file
        start_str = self.start_date_final.strftime("%d-%m-%y")
        end_str = self.end_date_final.strftime("%d-%m-%y")
        filename = f"{self.ticker}_Metrics_{start_str}_to_{end_str}.xlsx"

        with pd.ExcelWriter(filename) as writer:
            self.metrics.to_excel(
                writer, sheet_name="Model_Accuracy", index=False
            )  # Metrics sheet
            pred_df = pd.DataFrame(self.predictions)
            pred_df.index = [f"Day {i+1}" for i in range(self.forecast_days)]
            pred_df.to_excel(writer, sheet_name="Predictions")  # Predictions sheet

        st.success(f"Exported predictions and metrics to {filename}")  # Notify user

    def alert_changes(self):
        # Trigger alert if sharp price change is predicted
        alerts = []
        for name, pred in self.predictions.items():
            pct_change = ((pred[-1] - pred[0]) / pred[0]) * 100
            if abs(pct_change) > 2:
                alerts.append(
                    f"⚠️ ALERT: {name} predicts a change of {pct_change:.2f}% over {self.forecast_days} days!"
                )
        return alerts  # Return all alerts

    def open_news(self):
        # Open stock news on Google
        url = f"https://news.google.com/search?q={self.ticker}+stock"
        webbrowser.open(url)

    def get_predictions(self):
        return self.predictions  # Return stored predictions

    def get_metrics(self):
        return self.metrics  # Return evaluation metrics


# --- STREAMLIT UI INTERFACE ---

if __name__ == "__main__":
    st.title("📊 Real-Time Stock Teller Analyzer")  # App title

    # Input fields
    ticker = st.text_input("Enter Stock Ticker Symbol (e.g. TCS.BO, AAPL)", "AAPL")
    forecast_days = st.slider("Days to Predict Ahead", 1, 15, 5)
    show_news = st.checkbox("Show Latest Stock News")
    export_excel = st.checkbox("Export Predictions and Metrics to Excel")

    # Run button
    if st.button("Run Prediction"):
        predictor = StockPricePredictor(
            ticker, forecast_days
        )  # Create predictor object
        predictor.fetch_data()  # Step 1: Get data
        predictor.preprocess_data()  # Step 2: Prepare data
        predictor.train_models()  # Step 3: Train models
        predictor.predict_future()  # Step 4: Make predictions
        predictor.evaluate_models()  # Step 5: Evaluate
        predictor.visualize()  # Step 6: Visualize

        # Show analysis period
        start_fmt = predictor.start_date_final.strftime("%d-%m-%y")
        end_fmt = predictor.end_date_final.strftime("%d-%m-%y")
        st.markdown(f"### 📅 Analysis Period: From **{start_fmt}** to **{end_fmt}**")

        # Display outputs
        st.subheader("📈 Prediction Results")
        st.write(predictor.get_predictions())

        st.subheader("📊 Model Accuracy Metrics")
        st.dataframe(predictor.get_metrics())

        # Alerts if any
        alerts = predictor.alert_changes()
        if alerts:
            for alert in alerts:
                st.warning(alert)

        # Export to Excel
        if export_excel:
            predictor.export_results()

        # Download CSV
        st.subheader("📄 Download Raw Stock Data")
        predictor.save_data_csv()

        # Open news
        if show_news:
            predictor.open_news()
