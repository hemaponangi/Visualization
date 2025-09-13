import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("DV Assignment - Visualization Techniques")

# Load dataset (Iris)
st.write("### Sample Dataset: Iris")
df = sns.load_dataset("iris")
st.dataframe(df.head())

# Dropdown to choose chart
chart = st.selectbox(
    "Choose Visualization",
    ["Histogram (1D)", "Scatter Plot (2D)", "Line Plot (2D)", "3D Scatter Plot"]
)

if chart == "Histogram (1D)":
    col = st.selectbox("Select numeric column", df.select_dtypes(include=np.number).columns)
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=10, color="skyblue", edgecolor="black")
    ax.set_title(f"Histogram of {col}")
    st.pyplot(fig)

elif chart == "Scatter Plot (2D)":
    x = st.selectbox("X-axis", df.select_dtypes(include=np.number).columns)
    y = st.selectbox("Y-axis", df.select_dtypes(include=np.number).columns)
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y], c="blue", alpha=0.6)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(f"Scatter Plot: {x} vs {y}")
    st.pyplot(fig)

elif chart == "Line Plot (2D)":
    col = st.selectbox("Select numeric column", df.select_dtypes(include=np.number).columns)
    fig, ax = plt.subplots()
    ax.plot(df[col], marker="o", linestyle="-", color="green")
    ax.set_title(f"Line Plot of {col}")
    st.pyplot(fig)

else:  # 3D Scatter Plot
    from mpl_toolkits.mplot3d import Axes3D

    x = "sepal_length"
    y = "sepal_width"
    z = "petal_length"

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(df[x], df[y], df[z], c="red", marker="o")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    ax.set_title("3D Scatter Plot")
    st.pyplot(fig)
