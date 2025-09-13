import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Simple Data Visualization App")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read file
    df = pd.read_csv(uploaded_file)

    # Show data
    st.write("### Preview of Data")
    st.dataframe(df.head())

    # Select column for visualization
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_columns) > 0:
        col = st.selectbox("Select a column to visualize", numeric_columns)

        # Plot histogram
        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20, color='skyblue', edgecolor='black')
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)

        # Show line chart
        st.write("### Line Chart")
        st.line_chart(df[col])
    else:
        st.warning("No numeric columns found for visualization.")
else:
    st.info("👆 Upload a CSV file to get started.")


