from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
import os
import google.generativeai as genai

load_dotenv()

# MongoDB setup
mongodb_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongodb_uri)
db = client['genai']
collection = db['QA-chatbot']
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# api key setup
api_key = os.getenv("GEMINI_API_KEY")
if 'GEMINI_API_KEY' not in os.environ:
    raise ValueError("Environment variable GEMINI_API_KEY is not set.")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

#PDF
pdf=r"C:\Users\LENOVO\Desktop\Git\GenAI_QA_chatbot\GenAI-QA-ChatBot\Data_enger_interview_prep.pdf"