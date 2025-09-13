import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Heatmap Visualization App 🔥")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Data")
    st.dataframe(df.head())

    # Show correlation heatmap
    st.write("### Correlation Heatmap")
    corr = df.corr()

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)
else:
    st.info("Please upload a CSV file to see the heatmap.")

