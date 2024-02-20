import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

#Setup
st.set_page_config(
    layout="wide",
    page_title = "Housing Sale Price Prediction",
    page_icon="🏠",
    initial_sidebar_state="expanded"
)

show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Page("proposal.py", "Project Proposal", "📄"),
        Page("ganttChart.py", "Gantt Chart", "📝")
    ]
)

st.title("🏠 Home")

st.write("placeholder text")