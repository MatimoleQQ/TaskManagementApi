import pytest

def test_register_user(client):
    response = client.post("/users/", json={"email": "test@example.com", "password": "mypassword"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_register_duplicate_user(client):
    response = client.post("/users/", json={"email": "test@example.com", "password": "mypassword"})
    assert response.status_code == 400  # walidacja duplikatu

def test_login_user(client):
    response = client.post("/login", data={"username": "test@example.com", "password": "mypassword"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_password(client):
    response = client.post("/login", data={"username": "test@example.com", "password": "wrongpass"})
    assert response.status_code == 401