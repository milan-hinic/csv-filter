import pandas as pd
from datetime import datetime, timedelta
import streamlit as st

# App title
st.title("CSV Row Filter (Activation Date)")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    # Read CSV into a pandas DataFrame
    df = pd.read_csv(uploaded_file)
    st.write("Original Data:")
    st.dataframe(df)

    # Convert ActivationDate to datetime format
    df['ActivationDate'] = pd.to_datetime(df['ActivationDate'], errors='coerce')

    # Get today's date and calculate the date 7 days ago
    today = datetime.now()
    seven_days_ago = today - timedelta(days=7)

    # Filter rows where ActivationDate is within the last 7 days
    filtered_df = df[df['ActivationDate'] >= seven_days_ago]
    st.write("Filtered Data (Last 7 Days):")
    st.dataframe(filtered_df)

    # Download filtered data
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered CSV",
        data=csv,
        file_name="filtered_data.csv",
        mime="text/csv",
    )
