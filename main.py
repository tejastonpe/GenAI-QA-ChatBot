import streamlit as st
import os
from chatbot import  query_data

st.title("QA ChatBot")

query = st.text_input("Ask Question regarding Data Engineering:")
if st.button("Submit"):        
    if query:
        response = query_data(query)
        st.write("Answer:", response)