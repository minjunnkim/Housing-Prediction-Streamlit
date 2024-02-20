import pandas as pd
import streamlit as st
from st_pages import add_page_title
from st_aggrid import AgGrid
import xlsxwriter
from io import BytesIO

st.title("📝 Gantt Chart")

df = pd.read_excel("Proposal/GanttChart.xlsx", usecols = 'A:F')
AgGrid(df)

with open("Proposal/GanttChart.xlsx", "rb") as f:
    b = f.read()

st.download_button(label="Download the full Gantt Chart Spreadsheet",
                    data=b,
                    file_name="GanttChart.xlsx",
                    mime='application/octet-stream')