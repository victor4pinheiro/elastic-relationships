from elasticsearch import Elasticsearch
from flask import Flask, make_response

app = Flask(__name__)

@app.get("/")
def main():
    return make_response({ "message": "Main" }, 200)

if __name__ == "__main__":
    app.run(debug=True)
