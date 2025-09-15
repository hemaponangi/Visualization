import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Pie Chart Visualization")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Dataset Preview")
    st.write(df.head())

    # Select column for pie chart
    column = st.selectbox("Select a column for Pie Chart", df.columns)

    # Count values
    counts = df[column].value_counts()

    # Plot Pie Chart
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie is a circle.
    st.pyplot(fig)


