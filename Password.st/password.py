import streamlit as st
import re

st.set_page_config(page_title="Password-Strength-Checker")
st.title("Password Strength Checker – Stay Secure🔐")

st.write("◼Check your password strength in real-time—see if it can resist brute force attacks, guessing, & leaks.")
st.write("◼Get a detailed breakdown of your password weaknesses & tips to make it uncrackable")

password = st.text_input("Enter your Password:", type="password")

feedback = []
score = 0


if not password:
    st.info("Please enter your password to get started")
elif len(password) < 8:
    feedback.append("❌ Password should be at least 8 characters long")
    st.markdown("## IMPROVEMENT SUGGESTIONS")
    for tip in feedback:
        st.write(tip)
else:
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase characters")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit")

    if re.search(r'[!@#$%*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%*)")


    if score == 3:
        feedback.append("✅ Your password is strong! This would take years to break.")
    elif score == 2:
        feedback.append("🆗 Okay, but not strong enough. Add more random characters")
    else:
        feedback.append("🚫 This password is too weak! It can be cracked instantly.")

   
    if feedback:
        st.markdown("## IMPROVEMENT SUGGESTIONS")
        for tip in feedback:
            st.write(tip)