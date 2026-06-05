import streamlit as st
from cryptography.fernet import Fernet
import os

# Generate key if not exists
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Title
st.title("Secure Encryption & Decryption Tool")

# User input
message = st.text_area("Enter your message")

# Encrypt button
if st.button("Encrypt"):

    encrypted = fernet.encrypt(message.encode())

    st.success("Encrypted Message:")
    st.code(encrypted.decode())

# Decrypt section
encrypted_input = st.text_area("Enter encrypted message")

if st.button("Decrypt"):

    try:
        decrypted = fernet.decrypt(encrypted_input.encode())

        st.success("Decrypted Message:")
        st.code(decrypted.decode())

    except:
        st.error("Invalid encrypted message!")