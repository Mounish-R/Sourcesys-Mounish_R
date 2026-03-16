import streamlit as st

st.title("Streamlit App")

st.header("Welcome to My Page")

st.write("My Name is MOUNISH R")

st.image("Streamlit/assets/logo.jpg", caption="Sample Image")

name = st.text_input("Enter your name")

age = st.number_input("Enter your age", min_value=1, max_value=100)

language = st.selectbox(
    "Select your language",
    ["Tamil", "English", "Hindi", "Telugu", "Kannada"]
)

gender = st.radio(
    "Select your gender",
    ["Male", "Female", "Other"]
)

rating = st.slider("Rate this app", 1, 10)


if st.button("Submit"):
    st.success("Form Submitted Successfully")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Language:", language)
    st.write("Gender:", gender)
    st.write("Rating:", rating)


