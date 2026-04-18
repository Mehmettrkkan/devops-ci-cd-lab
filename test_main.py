from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mesaj": "CI/CD Pipeline basariyla calisiyor!"}

def test_topla():
    response = client.get("/topla/5/7")
    assert response.status_code == 200
    assert response.json() == {"sonuc": 12}
