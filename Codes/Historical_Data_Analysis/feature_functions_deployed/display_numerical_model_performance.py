# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to Display Model Performance

def display_numerical_model_performance():
    # HTML content
    html_content = """
    <h5>Regression Model Performance Overview</h5>
    <p class="description">This table presents the performance of various regression models for different companies. We have utilized an ensemble model approach to enhance prediction accuracy.</p>

    <table>
        <tr>
            <th>Company</th>
            <th>Linear Regression</th>
            <th>Ridge Regression</th>
            <th>Lasso Regression</th>
            <th>Elastic Net Regression</th>
        </tr>
        <tr>
            <td>Apple (AAPL)</td>
            <td>0.9998629224782566</td>
            <td>0.9998630076573156</td>
            <td>0.9993577928176817</td>
            <td>0.9996487306800625</td>
        </tr>
        <tr>
            <td>Amazon (AMZN)</td>
            <td>0.999084553005321</td>
            <td>0.9961820949085249</td>
            <td>0.9961820949085249</td>
            <td>0.9965084504390407</td>
        </tr>
        <tr>
            <td>Google (GOOG)</td>
            <td>0.9992315300913325</td>
            <td>0.9992317269769614</td>
            <td>0.9973035403402394</td>
            <td>0.9973876081990091</td>
        </tr>
        <tr>
            <td>Microsoft (MSFT)</td>
            <td>0.9992315300913325</td>
            <td>0.9998440164467663</td>
            <td>0.9993642265769165</td>
            <td>0.9994838523467628</td>
        </tr>
        <tr>
            <td>Meta (META)</td>
            <td>0.9992315300913325</td>
            <td>0.9992317269769614</td>
            <td>0.9973035403402394</td>
            <td>0.9973876081990091</td>
        </tr>
        <tr>
            <td>Netflix (NFLX)</td>
            <td>0.9992198305734726</td>
            <td>0.9992198288782033</td>
            <td>0.9971600744221598</td>
            <td>0.9971700356054888</td>
        </tr>
        <tr>
            <td>NVIDIA (NVDA)</td>
            <td>0.9971063606802831</td>
            <td>0.998365397592374</td>
            <td>0.9940339650281499</td>
            <td>0.9972701576306695</td>
        </tr>
        <tr>
            <td>Tata Consultancy Services (TCS)</td>
            <td>0.9979612118835919</td>
            <td>0.9979612934362246</td>
            <td>0.9890586523727406</td>
            <td>0.9891227853737217</td>
        </tr>
    </table>
    """

    # Display the HTML content
    st.markdown(html_content, unsafe_allow_html=True)
