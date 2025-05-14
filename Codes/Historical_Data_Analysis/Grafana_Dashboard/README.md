# 📊 Grafana Dashboard Setup Guide

This guide outlines how to install Grafana and connect it to the InfluxDB database to visualize historical stock market data.

## 🛠 Installation

### ✅ Windows

1. Download from: [https://grafana.com/grafana/download](https://grafana.com/grafana/download)
2. Extract and run `grafana-server.exe`.
3. Open `http://localhost:3000` in a browser.
4. Default login: `admin` / `admin` (you’ll be prompted to change it).

### ✅ Linux (Debian/Ubuntu)

```bash
sudo apt install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
sudo apt update
sudo apt install grafana
sudo systemctl start grafana-server
```

## 🔗 Connecting Grafana to InfluxDB

1. Go to **Settings > Data Sources** in Grafana.

2. Choose **InfluxDB** as the data source.

3. Enter:

   - URL: `http://localhost:8086`
   - Database(Bucket): `stock_price`
   - Auth Token (or username/password if InfluxQL)

4. Click **Save & Test**.

## 📈 Sample Dashboard

- Add new panel: Visualize `stock_price` by ticker.
- Example query:

```flux
from(bucket: "stock_price")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "stock_price")
```

## 🧩 Dashboard Features

- Real-time graphing of prices and volume
- Ticker-based filtering
- Export options (CSV/PNG/PDF)

## 📥 Import Prebuilt Dashboard

Once all the InfluxDB data upload scripts have been executed and your database is populated, you can import the prebuilt Grafana dashboard for this project:

1. In Grafana, go to **+ > Import**.
2. Upload the file `Stock Market Prediction-1731762228187.json`.
3. When prompted:

   - Set the **data source** to the InfluxDB instance you configured (ensure the name matches).

4. Click **Import**.

This will load a ready-to-use dashboard tailored for stock market data visualization.

## 📎 Notes

Ensure InfluxDB is running before launching Grafana. Use dashboard export/import to reuse panel layouts and backup configurations.
