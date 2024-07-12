import weaviate
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.openai import OpenAIEmbeddings

# Set these environment variables
# URL = os.getenv("WCS_URL")
# APIKEY = os.getenv("WCS_API_KEY")
  
# Connect to a WCS instance
weaviate_client = weaviate.connect_to_local()

