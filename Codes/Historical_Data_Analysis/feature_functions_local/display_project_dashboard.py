# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

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
         <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Overview/Dashboard_1.png" width="100%" alt="Stock Market Overview Snapshot 1" title="Stock Market Overview Snapshot 1" />
        <br><br>
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
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_1.png" width="100%" alt="Stock Market Overview Snapshot 1" title="Stock Market Overview Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_Panel_Dashboard_Description_and_Datasets_Information_View_1.png" width="100%" alt="Stock Market Overview Snapshot 2" title="Stock Market Overview Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_Panel_Dashboard_Description_and_Datasets_Information_View_2.png" width="100%" alt="Stock Market Overview Snapshot 3" title="Stock Market Overview Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_Panel_Stock_Market_View_1.png" width="100%" alt="Stock Market Overview Snapshot 4" title="Stock Market Overview Snapshot 4" />
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
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Numerical_Analysis/Dashboard_1.png" width="100%" alt="Numerical Analysis Snapshot 1" title="Numerical Analysis Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Numerical_Analysis/Dashboard_2.png" width="100%" alt="Numerical Analysis Snapshot 2" title="Numerical Analysis Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Numerical_Analysis/Dashboard_3.png" width="100%" alt="Numerical Analysis Snapshot 3" title="Numerical Analysis Snapshot 3" />
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
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_1.png" width="100%" alt="Model Prediction Snapshot 1" title="Model Prediction Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_2.png" width="100%" alt="Model Prediction Snapshot 2" title="Model Prediction Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_Panel_Model_Evaluation_View.png" width="100%" alt="Model Prediction Snapshot 3" title="Model Prediction Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_3.png" width="100%" alt="Model Prediction Snapshot 3" title="Model Prediction Snapshot 3" />
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
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Textual_Analysis/Dashboard_1.png" width="100%" alt="Textual Analysis Snapshot 1" title="Textual Analysis Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Textual_Analysis/Dashboard_2.png" width="100%" alt="Textual Analysis Snapshot 2" title="Textual Analysis Snapshot 2" />
        <br><br
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
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_1.png" width="100%" alt="Hybrid Model Snapshot 1" title="Hybrid Model Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_2.png" width="100%" alt="Hybrid Model Snapshot 2" title="Hybrid Model Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_3.png" width="100%" alt="Hybrid Model Snapshot 3" title="Hybrid Model Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_4.png" width="100%" alt="Hybrid Model Snapshot 4" title="Hybrid Model Snapshot 4" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )
