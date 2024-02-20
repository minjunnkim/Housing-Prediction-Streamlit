import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

st.title("📝 Gantt Chart")

df = pd.read_excel("Proposal/GanttChart.xlsx", usecols = 'A:F')
AgGrid(df)

with open("Proposal/GanttChart.xlsx", "rb") as f:
    b = f.read()

st.download_button(label="Download the full Gantt Chart",
                    data=b,
                    file_name="GanttChart.xlsx",
                    mime='application/octet-stream')