import streamlit as st
 
# Set the title of the web page
st.set_page_config(page_title="Simple Web Page with Tabs", layout="wide")
 
# Define the sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Reports"])
 
# Define content for each tab
 
if page == "Reports":
    st.title("Reports")
    st.write("Here are the Power BI reports.")
    # Embed Power BI report using an iframe
    report_url = " Enter your Power BI Service link"
    st.markdown(f'<<iframe title="Sales BI" width="1140" height="541.25" src=" Enter your Power BI Service link" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)