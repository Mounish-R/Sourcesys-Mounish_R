import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="CSV Analyzer", layout="wide")

st.title("CSV Dataset Analyzer")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read dataset
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Info")
    st.write("Shape:", df.shape)

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found in dataset.")
    else:
        st.subheader("Statistical Summary")
        st.dataframe(df[numeric_cols].describe())

        # Missing values
        st.subheader("Missing Values")
        missing = df.isnull().sum()
        st.write(missing)

        # Fill missing option
        if st.checkbox("Fill missing values with column mean"):
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
            st.success("Missing values filled!")

        # Column selection
        st.subheader("Select Columns for Analysis")
        col1 = st.selectbox("Select X-axis", numeric_cols)
        col2 = st.selectbox("Select Y-axis (optional)", [None] + numeric_cols)

        # Chart type
        chart_type = st.selectbox(
            "Choose Chart Type",
            ["Line Chart", "Bar Chart", "Histogram", "Scatter Plot"]
        )

        st.subheader("Visualization")

        fig, ax = plt.subplots()

        if chart_type == "Line Chart":
            ax.plot(df[col1])
            ax.set_title(f"Line Chart of {col1}")

        elif chart_type == "Bar Chart":
            ax.bar(df.index, df[col1])
            ax.set_title(f"Bar Chart of {col1}")

        elif chart_type == "Histogram":
            ax.hist(df[col1], bins=20)
            ax.set_title(f"Histogram of {col1}")

        elif chart_type == "Scatter Plot" and col2 is not None:
            ax.scatter(df[col1], df[col2])
            ax.set_xlabel(col1)
            ax.set_ylabel(col2)
            ax.set_title(f"Scatter Plot: {col1} vs {col2}")

        st.pyplot(fig)

else:
    st.info("Please upload a CSV file to begin.")