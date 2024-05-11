
def caesar_cipher(text, shift):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                cipher_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                cipher_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipher_text += char
    return cipher_text

# Streamlit web interface
import streamlit as st

def main():
    st.title("Caesar Cipher")

    # Input plaintext from the user
    plaintext = st.text_input("Enter plaintext:")

    # Input shift value from the user
    shift = st.number_input("Enter shift value:", value=3, step=1)

    # Apply Caesar Cipher
    if st.button("Encrypt"):
        if plaintext:
            encrypted_text = caesar_cipher(plaintext, shift)
            st.success(f"Encrypted text: {encrypted_text}")

if __name__ == "__main__":
    main()
