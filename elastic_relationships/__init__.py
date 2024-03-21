from os import getenv
from elasticsearch import Elasticsearch
from flask import Flask, make_response
from dotenv import load_dotenv


load_dotenv()

ELASTIC_USER = getenv("ELASTIC_USER") or "elastic"
ELASTIC_PASSWORD = getenv("ELASTIC_PASSWORD") or "SuperSecret"
ELASTIC_HOST = getenv("ELASTIC_HOST")

app = Flask(__name__)
db = Elasticsearch(
        ELASTIC_URL,
        basic_auth=(ELASTIC_USER, ELASTIC_PASSWORD),
        verify_certs=False
)

@app.post("/orders")
def create_order():
    
    test = { "message": "Main" }
    return make_response(test, 200)

@app.get("/")
def sample():
    return { "property": "teste" }

if __name__ == "__main__":
    app.run(debug=True)
