import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation  # Add special characters (#$%&*!@)

    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title('🔐Password Generator')

# Define the password generation parameters
length = st.slider('Select Password Length', min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Add Digits")
use_special = st.checkbox("Add Special Characters")

if st.button('Generate Password'):
    # Generate the password when the button is clicked
    password = generate_password(length, use_digits, use_special)
    st.write(f'🔓Generated Password: {password}')
