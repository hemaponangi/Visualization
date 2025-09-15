import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Correlation Heatmap Visualization")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Dataset Preview")
    st.write(df.head())

    # Keep only numeric columns
    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.shape[1] > 1:  # Need at least 2 numeric columns
        st.write("### Correlation Heatmap")

        corr = numeric_df.corr()

        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("The dataset must have at least two numeric columns for a heatmap.")


