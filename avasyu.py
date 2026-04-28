import streamlit as st
st.title("My first streamlit app")
st.write("Hello! Creating a simple web application using streamlit library.")
name = st.text_input("Enter your name :")
age= st.number_input("Enter your age")
if st.button ("Submit"):
   st.write("Hello, {name}! Welcome to streamlit.")
