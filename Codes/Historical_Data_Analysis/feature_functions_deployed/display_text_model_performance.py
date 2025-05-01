# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to Display Model Performance

def display_text_model_performance():
    # Basic HTML table without additional styling
    html_content = """
    <h5>Regression Model Performance Overview</h5>
    <p>This table presents the performance of various regression models for different companies.</p>

    <table border="1">
    <thead>
        <tr>
        <th>Metric</th>
        <th>Logistic Regression</th>
        <th>Naive Bayes</th>
        <th>Random Forest</th>
        </tr>
    </thead>
    <tbody>
        <td>Accuracy</td>
        <td>0.6516</td>
        <td>0.6672</td>
        <td>0.9900</td>
        </tr>
        <!-- Class 0 -->
        <tr>
        <td>Class 0 Precision</td>
        <td>0.62</td>
        <td>0.65</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Class 0 Recall</td>
        <td>0.82</td>
        <td>0.77</td>
        <td>1.00</td>
        </tr>
        <tr>
        <td>Class 0 F1-Score</td>
        <td>0.71</td>
        <td>0.70</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Class 0 Support</td>
        <td>2395</td>
        <td>2395</td>
        <td>2395</td>
        </tr>
        <!-- Class 1 -->
        <tr>
        <td>Class 1 Precision</td>
        <td>0.72</td>
        <td>0.70</td>
        <td>1.00</td>
        </tr>
        <tr>
        <td>Class 1 Recall</td>
        <td>0.48</td>
        <td>0.56</td>
        <td>0.98</td>
        </tr>
        <tr>
        <td>Class 1 F1-Score</td>
        <td>0.57</td>
        <td>0.62</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Class 1 Support</td>
        <td>2304</td>
        <td>2304</td>
        <td>2304</td>
        </tr>
        <!-- Overall Metrics -->
        <tr>
        <td>Macro Avg Precision</td>
        <td>0.67</td>
        <td>0.67</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Macro Avg Recall</td>
        <td>0.65</td>
        <td>0.67</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Macro Avg F1-Score</td>
        <td>0.64</td>
        <td>0.66</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Weighted Avg Precision</td>
        <td>0.67</td>
        <td>0.67</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Weighted Avg Recall</td>
        <td>0.65</td>
        <td>0.67</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Weighted Avg F1-Score</td>
        <td>0.64</td>
        <td>0.66</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Total Support</td>
        <td>4699</td>
        <td>4699</td>
        <td>4699</td>
        </tr>
    </tbody>
    </table>

    """

    # Display the HTML content
    st.markdown(html_content, unsafe_allow_html=True)
