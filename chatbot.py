import streamlit as st
from pdftovector import get_query_embedding
from connections import collection,db, model

def search_in_mongodb(query_vector):
    Aggregation_query = [
        {
            "$vectorSearch": {
                "queryVector": query_vector,
                "path": "question_embedding",
                "numCandidates": 100,
                "limit": 5,
                "index": "answer_search"
            }
        },
        {
            "$project": {
                "answer": 1,
                "_id": 0
            }
        }
    ]
    try:
        results = collection.aggregate(Aggregation_query)
        data_retrived = list(results)
        
        if not data_retrived:
            print("No Relevent Information found")
                
        return data_retrived
    except Exception as e:
        print("aggregation query error:", e)
        return []

def query_data(query):
    query_embedding = get_query_embedding(query)    
    results = search_in_mongodb(query_embedding)
    
    output = []
    for result in results:
        output.append(result['answer'])    
    response=get_exact_answer(output,query)
    return response

def get_exact_answer(data,query):
    if data:
        prompt = f"""
        Your task is to provide most exact answer from the data:
        data:{data}
        user query:{query}
        if data not found then give responce 'No Relavent Information found.
        If user query not found in database then give response 'Question not availabe in database'
        """
        response = model.generate_content(prompt)
        return response.text.strip()      
