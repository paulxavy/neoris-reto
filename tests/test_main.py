from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_devops_post_success():
    headers = {
        "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
        "Content-Type": "application/json"
    }
    payload = {
        "message": "Esto es un test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "timeToLifeSec": 45
    }
    response = client.post("/DevOps", json=payload, headers=headers)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Juan Perez your message will be send"}

def test_devops_invalid_apikey():
    headers = {
        "X-Parse-REST-API-Key": "jeje",
        "Content-Type": "application/json"
    }
    payload = {
        "message": "test",
        "to": "Juan",
        "from": "Rita",
        "timeToLifeSec": 10
    }
    response = client.post("/DevOps", json=payload, headers=headers)
    assert response.status_code == 403

def test_devops_methods_error():
    methods = ["get", "put", "delete", "patch"]
    for method in methods:
        call = getattr(client, method)
        response = call("/DevOps")
        assert response.text == '"ERROR"'