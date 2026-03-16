import streamlit as st
from pathlib import Path

st.title(" AI Career Path Predictor")

st.header("Discover Your Future Tech Career")

st.write("Answer a few questions and we will predict a suitable tech career for you.")

image_path = Path(__file__).parent / "assets" / "logo.jpg"
st.image(image_path, caption="Future Tech Careers")

name = st.text_input("Enter your name")

age = st.number_input("Enter your age", min_value=15, max_value=50)

interest = st.selectbox(
    "Which field interests you the most?",
    ["Artificial Intelligence", "Web Development", "Data Analysis", "Cyber Security", "Cloud Computing"]
)

learning_style = st.radio(
    "How do you like solving problems?",
    ["Logical thinking", "Creative design", "Data analysis", "Security challenges"]
)

skill_level = st.slider("Rate your programming skill", 1, 10)

if st.button("Predict Career"):

    st.success("Career Prediction Completed!")

    st.subheader("User Profile")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Interest:", interest)
    st.write("Problem Solving Style:", learning_style)
    st.write("Skill Level:", skill_level)

    st.subheader("Recommended Career")

    if interest == "Artificial Intelligence" and skill_level >= 6:
        career = "AI Engineer"
    elif interest == "Data Analysis":
        career = "Data Scientist"
    elif interest == "Web Development":
        career = "Full Stack Developer"
    elif interest == "Cyber Security":
        career = "Cyber Security Analyst"
    elif interest == "Cloud Computing":
        career = "Cloud Engineer"
    else:
        career = "Software Developer"

    st.success(f"Suggested Career: {career}")

   
    if skill_level <= 3:
        st.warning("Start learning programming basics and practice daily.")
    elif skill_level <= 7:
        st.info("Build real-world projects to improve your skills.")
    else:
        st.success("You are ready for advanced tech roles. Start contributing to projects!")