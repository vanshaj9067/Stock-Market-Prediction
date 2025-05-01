# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to display the Text Model Visualization section

def display_text_model_visualization():
    st.markdown(
        """
        <h3 style="text-align:center;">Text Model Visualization Overview</h3>
        <div style="font-size:18px; text-align:center;">
            Our text model visualization highlights the detailed outputs and predictions using interactive charts and plots.
        </div>
        <br>
        <h4 style="text-align:center;">Functionality of the Text Model Visualization</h4>
        <div style="font-size:16px; text-align:justify;">
            The section demonstrates how text-based prediction models, such as those for sentiment analysis or topic classification, visualize 
            their results. Users can select different models to visualize text data, analyze results, and explore comparative insights through 
            various interactive plots and metrics.
            <br><br>
            Below is a conceptual visualization of how the text model operates and displays outputs.
        </div>
        <br>
        
        <h4 style="text-align:center;">Snapshots from the Model Visualization</h4>
        
        <!-- Image 1 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Textual_Analysis\Plots\Most_Frequent_Words_in_News_Articles.png" width="100%" alt="Model Visualization Snapshot 1" title="Model Visualization Snapshot 1" />
            <br><br>
        </div>

        <!-- Image 2 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Textual_Analysis\Plots\Target_Variable_Distribution.png" width="100%" alt="Model Visualization Snapshot 2" title="Model Visualization Snapshot 2" />
            <br><br>
        </div>
        
        <!-- Image 3 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Textual_Analysis\Plots\Pie_Chart_Target_Variable_Distribution.png" width="100%" alt="Model Visualization Snapshot 2" title="Model Visualization Snapshot 2" />
            <br><br>
        </div>

        <!-- Image 4 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Textual_Analysis\Plots\Top_20_Important_Features_(TF-IDF_Terms).png" width="100%" alt="Model Visualization Snapshot 3" title="Model Visualization Snapshot 3" />
            <br><br>
        </div>
        
        """,
        unsafe_allow_html=True,
    )
