from os import getenv
from elasticsearch import Elasticsearch
from flask import Flask, Response, make_response, request
from dotenv import load_dotenv


load_dotenv()

ELASTIC_CERTS = getenv("ELASTIC_CERTS") or "http_ca.crt"
ELASTIC_USER = getenv("ELASTIC_USER") or "elastic"
ELASTIC_PASSWORD = getenv("ELASTIC_PASSWORD") or "SuperSecret"
ELASTIC_HOST = getenv("ELASTIC_HOST")

app = Flask(__name__)
db = Elasticsearch(
    ELASTIC_HOST, basic_auth=(ELASTIC_USER, ELASTIC_PASSWORD), ca_certs=ELASTIC_CERTS
)


def format_message(status: int, **kargs) -> Response:
    if kargs.get("error"):
        message = {"error": kargs.get("error")}
    else:
        message = {"message": kargs.get("message")}

    return make_response(message, status)


@app.post("/customers")
def create_customer() -> Response:
    data = request.get_json()

    try:
        customer_name = data["customerName"]
        contact_name = data["contactName"]
        country = data["country"]

        customer = {
            "customerName": customer_name,
            "contactName": contact_name,
            "country": country,
        }

        db.index(index="customers", body=customer)
    except Exception as e:
        return format_message(error=f"Error: {e}", status=400)

    return format_message(message="Customer created successfully", status=201)


@app.get("/")
def sample():
    return {"property": "teste"}


if __name__ == "__main__":
    app.run(debug=True)
