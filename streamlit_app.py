import streamlit as st
import pandas as pd

st.title("Student Performance Dashboard")

# Sample data
data = {
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

st.write("Student Data:")
st.dataframe(df)

st.bar_chart(df.set_index("Name"))
