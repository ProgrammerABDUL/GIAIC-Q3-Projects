import streamlit as st
import random
import string

# Page Setup
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")
st.write("Enter a password below and check its strength based on security criteria.")

# Input field
password_input = st.text_input("Enter your password", type="password")

# List of common weak passwords to reject
BLACKLISTED_PASSWORDS = ["password", "123456", "password123", "qwerty", "admin"]

# Function to check password strength
def evaluate_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    if password.lower() in BLACKLISTED_PASSWORDS:
        feedback.append("This password is too common and easily guessable.")
        score = 1  # Force to weak if blacklisted

    return score, feedback

# Function to generate a strong password
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if password_input:
    score, feedback = evaluate_password(password_input)

    if score <= 2:
        st.error("Password Strength: Weak")
    elif score <= 4:
        st.warning("Password Strength: Moderate")
    else:
        st.success("Password Strength: Strong")

    if feedback:
        st.info("Suggestions to improve your password:")
        for item in feedback:
            st.markdown(f"- {item}")

# Password generator section
st.markdown("---")
st.subheader("🔧 Generate a Strong Password")
gen_length = st.slider("Select password length", min_value=8, max_value=24, value=12)

# Generate password on button click
if st.button("Generate Password"):
    generated = generate_password(gen_length)
    st.code(generated, language="text")
    st.success("Copy and use this password!")