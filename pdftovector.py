from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from connections import api_key,mongodb_uri,collection,db
from connections import pdf

def get_pdf_text(pdf): 
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_questions_answers(text):
    qa_pairs = []
    lines = text.split('\n')
    question = ""
    answer = ""
    for line in lines:
        if line.strip().endswith('?'):
            if question and answer:
                qa_pairs.append({"question": question, "answer": answer.strip()})
            question = line.strip()
            answer = ""
        else:
            answer += " " + line.strip()
    if question and answer:
        qa_pairs.append({"question": question, "answer": answer.strip()})
    return qa_pairs

def get_vector_store(qa_pairs):
    embedding_method=GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key)
    for qa in qa_pairs:
        print(qa)
        embedding=embedding_method.embed_documents([qa['question']])
        collection.insert_one({            
            "question_embedding":embedding[0],
            "answer":qa['answer']
        })

def pdftext_to_vector(pdf):  
    text = get_pdf_text(pdf)
    qa_pairs = extract_questions_answers(text)
    get_vector_store(qa_pairs)
    print(f'PDF text converted to vector')

def get_query_embedding(query):
    embedding_method = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    embedding = embedding_method.embed_documents([query])
    return embedding[0]

# pdftext_to_vector(pdf)