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

    # Select categorical column for grouping
    column = st.selectbox("Select a categorical column for Pie Chart", df.columns)

    # If dataset has numeric values, allow user to pick one to aggregate
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
    agg_col = None
    if numeric_cols:
        agg_col = st.selectbox("Select a numeric column to sum for Pie Chart (optional)", numeric_cols)

    # Aggregate data
    if agg_col:
        counts = df.groupby(column)[agg_col].sum()
    else:
        counts = df[column].value_counts()

    # Plot Pie Chart
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie is a circle.
    st.pyplot(fig)
