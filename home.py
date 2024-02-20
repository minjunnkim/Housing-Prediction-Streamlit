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
        
        Section("Project Proposal", icon="📄"),
        Page("proposal.py", "Project Proposal", "📄", in_section=True),
        Page("ganttChart.py", "Gantt Chart", "📝", in_section=True)
    ]
)

st.title("🏠 Home")

st.write("placeholder text")