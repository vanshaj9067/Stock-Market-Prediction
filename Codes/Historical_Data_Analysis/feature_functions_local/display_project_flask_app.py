# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to display the Flask App section


def display_project_flask_app():
    st.markdown(
        """
        <h3 style="text-align:center;">Flask App Overview</h3>
        <div style="font-size:18px; text-align:center;">
            Our Flask app is designed with a pastel lavender pink theme for a visually soothing user interface.
        </div>
        <br>
        <h4 style="text-align:center;">Flask App Functionality</h4>
        <div style="font-size:16px; text-align:justify;">
            The Flask application loads pre-trained models for each company, with separate models created to forecast stock prices. 
            Users can select a company from a dropdown menu, and the app fetches the appropriate model for predictions. The app 
            takes input data for open, high, low, and volume prices and displays the predicted close value.
            <br><br>
            Below is a visual representation of the Flask app's architecture.
        </div>
        <br>
        
        <!-- Image for Flask App Logo -->
        <div style="text-align:center;">
            <img src="https://www.seekpng.com/png/full/875-8753366_flask-png.png" width="150" title="Flask Logo" alt="Flask Logo" />
            <br><br>
        </div>
        
        <!-- Image for Flask App Architecture -->
        <div style="text-align:center;">
            <img src="https://th.bing.com/th/id/OIP.zUyMlO4bXyV_GNy3XcFubgHaEC?rs=1&pid=ImgDetMain" width="400" title="Flask App Architecture" alt="Flask App Architecture" />
            <br><br>
        </div>
        
        <h4 style="text-align:center;">Snapshots from the Flask App</h4>
        
        <!-- Image 1 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/App_Snapshots/Flask_App/App_View_1.png" width="100%" alt="Flask App Snapshot 1" title="Flask App Snapshot 1" />
            <br><br>
        </div>

        <!-- Image 2 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/App_Snapshots/Flask_App/App_View_2.png" width="100%" alt="Flask App Snapshot 2" title="Flask App Snapshot 2" />
            <br><br>
        </div>

        <!-- Image 3 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/App_Snapshots/Flask_App/App_View_3.png" width="100%" alt="Flask App Snapshot 3" title="Flask App Snapshot 3" />
            <br><br>
        </div>
        
        """,
        unsafe_allow_html=True,
    )
