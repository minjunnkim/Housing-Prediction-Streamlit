import pandas as pd
import streamlit as st
from st_pages import add_page_title
from st_aggrid import AgGrid

st.title("📝 Gantt Chart")

df = pd.read_excel("Proposal/GanttChart.xlsx", usecols = 'A:F')
AgGrid(df)

