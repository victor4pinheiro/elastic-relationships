from elastic_relationships import app 


def test_create_orders():
    response = app.test_client().post('/orders')
    json = response.get_json()

    assert response.status_code == 201
    assert json["message"] == "Order created successfully"
