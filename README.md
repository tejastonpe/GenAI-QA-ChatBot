# Question Answer Chatbot
This repository contains the code for a Question Answer (QA) Chatbot. The chatbot is designed to answer questions based on a set of predefined questions and answers stored in a vector database. The web interface is built using Streamlit, and the backend MongoDB Atlas for storage and the Gemini API for generating responses.

### Features
* **Streamlit Web Interface:** A simple and interactive web interface for users to ask questions and receive answers.
* **PDF Conversion:** Convert QA PDFs into a vector database by embedding questions.
* **MongoDB Atlas:** Store the embedded questions & text format answers in MongoDB Atlas for efficient retrieval.
* **Gemini API Integration:** Use the Gemini API to provide accurate answers based on the prompt.

### Project Structure
* **main.py:** Main file to run the Streamlit web application.
* **pdftovector.py:** Contains functions for processing and embedding questions from PDFs.
* **connections.py:** Functions for interacting with MongoDB Atlas and Gemini API
* **chatbot.py:** contains searching answer from database to give answers
* **.env:** Environment variables for API keys and database connections.
