# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to Display Model Performance

def display_hybrid_model_performance():
    # Basic HTML table without additional styling
    html_content = """
    <h5>Regression Model Performance Overview</h5>
    <p>This table presents the performance of various regression models for different companies.</p>

    <table border="1">
    <thead>
        <tr>
        <th>Model</th>
        <th>MAE</th>
        <th>MSE</th>
        <th>RMSE</th>
        <th>R² Score</th>
        <th>Accuracy (%)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td>MLP</td>
        <td>4.631412</td>
        <td>30.276025</td>
        <td>5.502365</td>
        <td>0.583915</td>
        <td>99.863574</td>
        </tr>
        <tr>
        <td>Linear Regression</td>
        <td>5.725293</td>
        <td>39.196283</td>
        <td>6.260694</td>
        <td>0.461323</td>
        <td>100.000000</td>
        </tr>
        <tr>
        <td>K-Nearest Neighbors (KNN)</td>
        <td>5.575181</td>
        <td>41.867105</td>
        <td>6.470479</td>
        <td>0.424618</td>
        <td>100.000000</td>
        </tr>
        <tr>
        <td>SVM</td>
        <td>5.771079</td>
        <td>47.432490</td>
        <td>6.887125</td>
        <td>0.348132</td>
        <td>99.454297</td>
        </tr>
        <tr>
        <td>Gradient Boosting</td>
        <td>6.189361</td>
        <td>52.197185</td>
        <td>7.224762</td>
        <td>0.282651</td>
        <td>100.000000</td>
        </tr>
        <tr>
        <td>Random Forest</td>
        <td>6.378920</td>
        <td>60.091005</td>
        <td>7.751839</td>
        <td>0.174165</td>
        <td>100.000000</td>
        </tr>
        <tr>
        <td>Decision Tree</td>
        <td>6.405307</td>
        <td>61.140660</td>
        <td>7.819249</td>
        <td>0.159740</td>
        <td>100.000000</td>
        </tr>
        <tr>
        <td>AdaBoost</td>
        <td>7.360769</td>
        <td>77.328544</td>
        <td>8.793665</td>
        <td>-0.062731</td>
        <td>100.000000</td>
        </tr>
    </tbody>
    </table>

    """

    # Display the HTML content
    st.markdown(html_content, unsafe_allow_html=True)
