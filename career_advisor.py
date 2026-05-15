import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🎯 Smart Career Advisor")
st.write("Enter your skills and get AI-powered career guidance!")

skills = st.text_input("Enter your skills (e.g. Python, SQL, Excel)")
experience = st.text_input("Years of experience (e.g. 0, 1, 2)")

if st.button("Get Career Advice"):
    with st.spinner("AI is analysing your profile..."):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an expert career advisor. Give structured, practical career advice."},
                {"role": "user", "content": f"My skills are: {skills}. I have {experience} years of experience. Suggest: 1) Best job roles for me 2) Skill gaps I should fill 3) Learning path for next 6 months"}
            ]
        )
        st.write(response.choices[0].message.content)