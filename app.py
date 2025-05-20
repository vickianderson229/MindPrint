import streamlit as st
from mindprint_detector import detect_ai_likelihood, get_feedback

st.title("MindPrint – Student Essay Checker")

user_text = st.text_area("✍️ Paste your student essay below:")

if user_text:
    if st.button("Check AI Likelihood"):
        likelihood_score, explanation = detect_ai_likelihood(user_text)
        st.write(f"🧠 **AI Likelihood Score:** {likelihood_score * 100:.2f}%")
        st.markdown(f"**Explanation:** {explanation}")

    if st.button("Generate Feedback"):
        likelihood_score, _ = detect_ai_likelihood(user_text)
        feedback = get_feedback(user_text, likelihood_score)
        st.markdown("### 📝 Feedback:")
        st.write(feedback)
