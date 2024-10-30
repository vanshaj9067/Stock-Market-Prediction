# Stock-Market-Prediction

This repository is for our 7th-semester minor project titled **Advanced Stock Price Forecasting Using a Hybrid Model of Numerical and Textual Analysis**.

![Stock Market Illustration](https://github.com/user-attachments/assets/f5751f74-43c5-4045-aa9f-bb7abd19c1aa)

## Current Progress

For the project **Advanced Stock Price Forecasting Using a Hybrid Model of Numerical and Textual Analysis**, we have made significant strides in multiple areas:

1. **Data Collection and Storage**: We are working with historical stock data of major companies. This data has been transferred into an InfluxDB database, allowing us to handle extensive time-series data efficiently.

2. **Data Visualization**: We have set up a Grafana dashboard, which will enable real-time visualization of stock prices and analysis outcomes as we advance in our model development.

3. **Textual Analysis for Enhanced Forecasting**: For textual analysis, we are leveraging Natural Language Processing (NLP) libraries, including NLTK and spaCy, to extract relevant insights from financial news and reports. This component will complement the numerical analysis, improving the accuracy of our hybrid forecasting model.

4. **Machine Learning**: We are currently exploring advanced machine learning models like ARIMA, LSTM, and Transformer, focusing on both the numerical and textual data components to form a comprehensive prediction model.

5. **Collaboration and Project Management**: The project repository on GitHub is up and running with all team members on board. We've organized tasks efficiently to promote seamless collaboration and effective version control.

---

## Dataset Used

| Company                           | Description                                                                                     | Data Range           | Dataset Shape | Starting Stock Date | Current Stock Date | Starting Stock Price | Current Stock Price |
|-----------------------------------|-------------------------------------------------------------------------------------------------|----------------------|---------------|---------------------|--------------------|----------------------|----------------------|
| <img src="https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-suite-everything-you-need-know-about-google-newest-0.png" height="40"> <br> Alphabet Inc. (Google) [GOOG] | Specializes in Internet-related services and products, including search engines, online advertising, and cloud computing. | 2014-03-27 : 2024-10-17 | (2659, 5) | 2014-03-27          | 2024-10-17         | $27.8542             | $164.51              |
| <img src="https://pngimg.com/uploads/amazon/amazon_PNG5.png" height="40"> <br> Amazon.com Inc. [AMZN]    | Started as an online bookstore, now a leader in e-commerce and cloud computing through AWS. | 1997-05-16 : 2024-10-17 | (6901, 5) | 1997-05-16          | 2024-10-17         | $0.0863              | $187.53              |
| <img src="https://th.bing.com/th/id/R.0ac491574e7ddb71dc2cab65a8bb501f?rik=5NzURUJ1L37UYg&riu=http%3a%2f%2fpurepng.com%2fpublic%2fuploads%2flarge%2fpurepng.com-apple-logologobrand-logoiconslogos-251519938788qhgdl.png&ehk=kQ%2bTI4imrP%2fg9UWIfehFMJOqAn1A3RQTROHV%2f1ORknk%3d&risl=&pid=ImgRaw&r=0" height="40"> <br> Apple Inc. [AAPL]   | Renowned for innovative consumer electronics, software, and services, including the iPhone and Mac computers. | 1980-12-12 : 2024-10-17 | (11053, 5) | 1980-12-12          | 2024-10-17         | $0.0992              | $232.15              |
| <img src="https://static.vecteezy.com/system/resources/previews/024/273/862/original/meta-logo-transparent-free-png.png" height="40"> <br> Meta Platforms [META] | Owner of Facebook, a global leader in social media and digital advertising. | 2012-05-18 : 2024-10-17 | (3124, 5) | 2012-05-18          | 2024-10-17         | $38.1174             | $576.93              |
| <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" height="40"> <br> Microsoft Corp. [MSFT] | A leading developer of software, consumer electronics, and personal computers. | 1986-03-13 : 2024-10-17 | (9728, 5) | 1986-03-13          | 2024-10-17         | $0.0603              | $416.72              |
| <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" height="40"> <br> Netflix Inc. [NFLX] | Global streaming entertainment service with a vast library of TV series and films. | 2002-05-23 : 2024-10-17 | (5640, 5) | 2002-05-23          | 2024-10-17         | $1.1964              | $687.65              |
| <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/235_Nvidia_logo-512.png" height="40"> <br> Nvidia Corp. [NVDA] | Specializes in graphics processing units and AI technology. | 1999-01-22 : 2024-10-17 | (6477, 5) | 1999-01-22          | 2024-10-17         | $0.0377              | $136.93              |
| <img src="https://companieslogo.com/img/orig/TCS.NS-7401f1bd.png?t=1631949260" height="40"> <br> Tata Consultancy Services [TCS] | Leading global IT services, consulting, and business solutions provider. | 2013-11-01 : 2024-10-17 | (2758, 5) | 2013-11-01          | 2024-10-17         | $543.0               | $11.8                |

## Resources
1. **Partial Data Analysis**:
   - Historical Stock Prices: [Yahoo Finance](https://finance.yahoo.com/)
   - Textual Data: [Textual Dataset](https://bit.ly/36fFPI6)

2. **Complete Historical Data**:
  - **Alphabet (Google) (GOOG)**: [Google Stock Price](https://www.macrotrends.net/stocks/charts/GOOG/google/stock-price-history)
   - **Apple (AAPL)**: [Apple Stock Price](https://www.macrotrends.net/stocks/charts/AAPL/apple/stock-price-history)
   - **Amazon (AMZN)**: [Amazon Stock Price](https://www.macrotrends.net/stocks/charts/TCS/container-store/stock-price-history)
   - **Meta (META)**: [Meta Stock Price](https://www.macrotrends.net/stocks/charts/META/meta-platforms/stock-price-history)
   - **Netflix (NFLX)**: [Netflix Stock Price](https://www.macrotrends.net/stocks/charts/NFLX/netflix/stock-price-history)
   - **Nvidia (NVDA)**: [Nvidia Stock Price](https://www.macrotrends.net/stocks/charts/NVDA/nvidia/stock-price-history)
   - **Microsoft (MSFT)**: [Microsoft Stock Price](https://www.macrotrends.net/stocks/charts/MSFT/microsoft/stock-price-history)
   - **TCS**: [TCS Stock Price](https://www.macrotrends.net/stocks/charts/TCS/container-store/stock-price-history)

---

## Project Database & Dashboard

For easy visualization and data management, we are using the following tools:

1. **InfluxDB Database**: Efficient time-series storage for handling historical and live data of large-volume stocks.

*Images of the InfluxDB Database will be added below:*

 ![InfluxDB Database Overview](https://github.com/user-attachments/assets/48cf5842-3637-4842-9081-95491ad8770f)
   
3. **Grafana Dashboard**: Providing a dynamic interface to view and interact with real-time forecasting results.

*Images of the Grafana Dashboard will be added below:*
   
![Grafana Dashboard - Detailed Analysis](https://github.com/user-attachments/assets/6de571a7-d831-439d-aac3-5bbc3751b960)
   <br>
   ![Grafana Dashboard - Overview 1](https://github.com/user-attachments/assets/c1b8d258-cb11-40de-8fce-aa9ca09bb133)
   <br>
![Grafana Dashboard - Overview 2](https://github.com/user-attachments/assets/872095f8-5f1d-45fa-abd0-159e76c9eede)
