import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Correlation Heatmap Visualization")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Dataset Preview")
    st.write(df.head())

    # Keep only numeric columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    if numeric_df.shape[1] > 1:  # Need at least 2 numeric columns
        corr = numeric_df.corr()

        st.write("### Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Dataset must have at least 2 numeric columns for a heatmap.")

