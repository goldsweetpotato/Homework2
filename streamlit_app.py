import streamlit as st
from transformers import pipeline
st.title("My AI Assistant")
user_prompt=st.text_input("user's prompt")
token_length=st.text_input("token length")
generator=pipeline('text-generation', model= "gpt2")
prompt = st.text_input()
output= generator(prompt, max_length=token_length, num_return_squences=10, truncation=true)[0]
st.write(output("generated_text"))
