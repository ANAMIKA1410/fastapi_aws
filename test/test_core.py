from fastapi.testclient import TestClient
from api.main import app

Client= TestClient(app)

def test_root():
    response=Client.get("/")
    assert response.status_code==200
    assert response.json()=={"message":"Hello world"}