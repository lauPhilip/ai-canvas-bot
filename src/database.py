import streamlit as st
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_mongodb_client():
    # Uses local .env or Streamlit Cloud Secrets
    uri = os.getenv("MONGO_URI") or st.secrets["MONGO_URI"]
    return MongoClient(uri)