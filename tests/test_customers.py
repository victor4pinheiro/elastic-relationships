from elastic_relationships import app

current_test = app.test_client()


def test_create_customers():
    body = {
        "customerName": "Alfred",
        "contactName": "Maria",
        "country": "Germany",
    }
    response = current_test.post("/customers", json=body)
    json = response.get_json()

    assert response.status_code == 201
    assert json["message"] == "Customer created successfully"
