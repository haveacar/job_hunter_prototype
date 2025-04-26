import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory.

def load_env():
    _ = load_dotenv(find_dotenv())


load_env()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENVIRONMENT = os.getenv('PINECONE_ENVIRONMENT')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')