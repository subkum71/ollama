## Make REG System
## 1. Use allready stored PDF in Chroma
## Basic Flow of system
## User Query-->Embeding-->Semantic Serach by entering Embedigg-->Search Result + User Query-->LLM-->Response to user

import ollama
from  sentence_transformers import SentenceTransformer 
import chromadb

# Constant
LLM_Model_name ="qwen3-vl:4b"
Embedding_Model="all-MiniLM-L6-v2"
CHROMA_PATH = r"D:\My-Study\Practice\Python\ChromaDB\chroma_db"
COLLECTION_NAME = "employee_policy"

#Keep User Query
User_Query=""

# Get User Query Embeding
def Get_Userquery_Embeddings(userquery):
    embedding_model = SentenceTransformer(
    Embedding_Model
    )
    query_embedding = embedding_model.encode(userquery).tolist()
    return query_embedding
# Get Search Results
def get_SearchResult(Query_embeddinglist,  topresult=1):
    print("Wait processing your query ... ")
      ## Connect to Chromadb
    client = chromadb.PersistentClient(
      path=CHROMA_PATH
    )
    collection = client.get_collection(
      name=COLLECTION_NAME
      )
      
    results = collection.query(
          query_embeddings=Query_embeddinglist,
          n_results=topresult
      )
    return(results)

  #-----------------Calling Main---------------------------#
  
print("Enter your question, type exit to end session")
while True:

    User_Query = input("\nYou: ")

    if User_Query.lower() == "exit":
        break
    print ("Wait getting semantic search results")
    answers= get_SearchResult(Get_Userquery_Embeddings(User_Query))
    print("Semantic Search Data:")
    if answers :
        print( answers["documents"][0])
    else:
        print("No result from semantic search")
        