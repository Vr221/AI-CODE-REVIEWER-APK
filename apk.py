import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyAYBSadaJEhspMTinbki7HCjG5q4nV_6ao")

system_prompt = """You are a Python code reviewer. You should review the code, identify errors,
provide improvements, and give a rating out of 5. Only accept Python code as input."""

gemini = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)


st.title(" Python Code Reviewer with Gemini AI")
st.write("Enter your Python code snippet below, and the AI will review it.")


user_prompt = st.text_area(" Enter your Python code:", height=250)

if st.button(" Review Code"):
    if user_prompt.strip():
        with st.spinner("Reviewing your code... ⏳"):
            response = gemini.generate_content(user_prompt, stream=True)

        # Display AI Review
        st.subheader("✅AI Review:")
        for chunk in response:
            st.write(chunk.text)
    else:
        st.warning("⚠️ Please enter a Python code snippet first.")