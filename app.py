import streamlit as st
from prompts import prompt_template_preferences, fallback_prompt
from logic import map_to_career_path, generate_explanation, needs_clarification
from mistral_model import generate_followup

st.set_page_config(page_title="Career Recommender with Mistral", page_icon="🎓")
st.title("🎯 Career Path Recommender (Powered by Mistral)")
st.write("Discover your ideal career path based on your interests!")

st.markdown("### 🧠 Tell us about yourself:")
st.info(prompt_template_preferences.strip())

user_input = st.text_area("Your Response", height=150)

if st.button("Get Recommendation") and user_input:
    mapped_paths = map_to_career_path(user_input)
    
    if needs_clarification(mapped_paths):
        st.warning("I'm not quite sure about your preferences yet.")
        st.markdown("#### 🤖 Mistral Suggests:")
        st.info(generate_followup(user_input))
    else:
        st.success("Based on your input, here are some career paths that may suit you:")
        st.markdown(generate_explanation(mapped_paths))
