# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to display the company data table with logos and details

def display_company_data_table():
    st.markdown(
        """
    <h4>This are all the datasets that are used in the analysis.</h4>

    <table style="width:100%; border-collapse:collapse;">
        <thead>
            <tr style="border-bottom:1px solid #ddd; text-align:left;">
                <th>Company</th>
                <th>Description</th>
                <th>Data Range</th>
                <th>Dataset Shape</th>
                <th>Starting Stock Date</th>
                <th>Current Stock Date</th>
                <th>Starting Stock Price</th>
                <th>Current Stock Price</th>
            </tr>
        </thead>
        <tbody>
            <!-- Google -->
            <tr>
                <td><img src="https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-suite-everything-you-need-know-about-google-newest-0.png"
                        height="40" /> <br> Alphabet Inc. (Google) [GOOG]</td>
                <td>Specializes in Internet-related services and products, including search engines, online advertising, and
                    cloud computing.</td>
                <td>2014-03-27 : 2024-10-17</td>
                <td>(2659, 5)</td>
                <td>2014-03-27</td>
                <td>2024-10-17</td>
                <td>$27.8542</td>
                <td>$164.51</td>
            </tr>
            <!-- Amazon -->
            <tr>
                <td><img src="https://pngimg.com/uploads/amazon/amazon_PNG5.png" height="40" /> <br> Amazon.com Inc. [AMZN]
                </td>
                <td>Started as an online bookstore, now a leader in e-commerce and cloud computing through AWS.</td>
                <td>1997-05-16 : 2024-10-17</td>
                <td>(6901, 5)</td>
                <td>1997-05-16</td>
                <td>2024-10-17</td>
                <td>$0.0863</td>
                <td>$187.53</td>
            </tr>
            <!-- Apple -->
            <tr>
                <td><img src="https://th.bing.com/th/id/R.0ac491574e7ddb71dc2cab65a8bb501f?rik=5NzURUJ1L37UYg&riu=http%3a%2f%2fpurepng.com%2fpublic%2fuploads%2flarge%2fpurepng.com-apple-logologobrand-logoiconslogos-251519938788qhgdl.png&ehk=kQ%2bTI4imrP%2fg9UWIfehFMJOqAn1A3RQTROHV%2f1ORknk%3d&risl=&pid=ImgRaw&r=0"
                        height="40" /> <br> Apple Inc. [AAPL]</td>
                <td>Renowned for innovative consumer electronics, software, and services, including the iPhone and Mac
                    computers.</td>
                <td>1980-12-12 : 2024-10-17</td>
                <td>(11053, 5)</td>
                <td>1980-12-12</td>
                <td>2024-10-17</td>
                <td>$0.0992</td>
                <td>$232.15</td>
            </tr>
            <!-- Meta Platforms -->
            <tr>
                <td><img src="https://static.vecteezy.com/system/resources/previews/024/273/862/original/meta-logo-transparent-free-png.png"
                        height="40" /> <br> Meta Platforms [META]</td>
                <td>Owner of Facebook, a global leader in social media and digital advertising.</td>
                <td>2012-05-18 : 2024-10-17</td>
                <td>(3124, 5)</td>
                <td>2012-05-18</td>
                <td>2024-10-17</td>
                <td>$38.1174</td>
                <td>$576.93</td>
            </tr>
            <!-- Microsoft -->
            <tr>
                <td><img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" height="40" /> <br>
                    Microsoft Corp. [MSFT]</td>
                <td>A leading developer of software, consumer electronics, and personal computers.</td>
                <td>1986-03-13 : 2024-10-17</td>
                <td>(9728, 5)</td>
                <td>1986-03-13</td>
                <td>2024-10-17</td>
                <td>$0.0603</td>
                <td>$416.72</td>
            </tr>
            <!-- Netflix -->
            <tr>
                <td><img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" height="40" /> <br>
                    Netflix Inc. [NFLX]</td>
                <td>Global streaming entertainment service with a vast library of TV series and films.</td>
                <td>2002-05-23 : 2024-10-17</td>
                <td>(5640, 5)</td>
                <td>2002-05-23</td>
                <td>2024-10-17</td>
                <td>$1.1964</td>
                <td>$687.65</td>
            </tr>
            <!-- Nvidia -->
            <tr>
                <td><img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/235_Nvidia_logo-512.png"
                        height="40" /> <br> Nvidia Corp. [NVDA]</td>
                <td>Specializes in graphics processing units and AI technology.</td>
                <td>1999-01-22 : 2024-10-17</td>
                <td>(6477, 5)</td>
                <td>1999-01-22</td>
                <td>2024-10-17</td>
                <td>$0.0377</td>
                <td>$136.93</td>
            </tr>
            <!-- Tata Consultancy Services (TCS) -->
            <tr>
                <td><img src="https://companieslogo.com/img/orig/TCS.NS-7401f1bd.png?t=1631949260" height="40" /> <br> Tata
                    Consultancy Services [TCS]</td>
                <td>Leading global IT services, consulting, and business solutions provider.</td>
                <td>2013-11-01 : 2024-10-17</td>
                <td>(2758, 5)</td>
                <td>2013-11-01</td>
                <td>2024-10-17</td>
                <td>$543.0</td>
                <td>$11.8</td>
            </tr>
        </tbody>        
    </table>
    """,
        unsafe_allow_html=True,
    )
