# Importing Streamlit for building the web-based interactive application framework
import streamlit as st


# Function to display the Reddit Chatbot Visualization section
def display_reddit_chatbot_visualization():
    """
    Displays the visualization section for the Reddit Chatbot.
    This section fetches and visualizes various plots derived from Reddit discussions,
    highlighting company mentions, sentiment analysis, word clouds, and word count distributions.
    """

    # Overview section for Reddit Chatbot Visualization
    st.markdown(
        """
        <h3 style="text-align:center;">Reddit Chatbot Visualization Overview</h3>
        <div style="font-size:18px; text-align:center;">
            This section showcases interactive visualizations from Reddit comments using the Reddit Chatbot.
            Explore company mentions, sentiment categories, word clouds, and more, to gain insights from Reddit discussions.
        </div>
        <br>
        <h4 style="text-align:center;">Functionality of Reddit Chatbot Visualization</h4>
        <div style="font-size:16px; text-align:justify;">
            This visualization highlights the insights extracted from Reddit data using the chatbot model. Users can explore various plots
            such as company mentions, sentiment distributions, word clouds, and more. The interactive nature of these plots allows 
            for in-depth analysis of Reddit discussions across different metrics.
            <br><br>
            Below are several snapshots from the Reddit Chatbot's analysis and visualizations.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    # Display the images directly from the GitHub repository without titles
    st.markdown(
        """
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Reddit_Chatbot/Plots/Company_Mentions_(Excluding_Other).png" width="100%" alt="Company Mentions (Excluding Other)" />
            <br><br>
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Reddit_Chatbot/Plots/Sentiment_Categories_Pie_Chart.png" width="100%" alt="Sentiment Categories Pie Chart" />
            <br><br>
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Reddit_Chatbot/Plots/Sentiment_Score_Distribution.png" width="100%" alt="Sentiment Score Distribution" />
            <br><br>
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Reddit_Chatbot/Plots/Word_Cloud_of_Reddit_Comments.png" width="100%" alt="Word Cloud of Reddit Comments" />
            <br><br>
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Reddit_Chatbot/Plots/Word_Count_Distribution.png" width="100%" alt="Word Count Distribution" />
        </div>
        """,
        unsafe_allow_html=True,
    )
