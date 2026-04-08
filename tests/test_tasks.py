import pytest

def get_token(client):
    response = client.post("/login", data={"username": "test@example.com", "password": "mypassword"})
    return response.json()["access_token"]

def test_create_task(client):
    token = get_token(client)
    response = client.post(
        "/tasks/",
        json={"title": "Test Task", "description": "Test Desc"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["completed"] is False

def test_get_tasks(client):
    token = get_token(client)
    response = client.get(
        "/tasks/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_delete_task(client):
    token = get_token(client)
    # Dodaj task
    response = client.post(
        "/tasks/",
        json={"title": "Delete Task", "description": "Delete Desc"},
        headers={"Authorization": f"Bearer {token}"}
    )
    task_id = response.json()["id"]

    # Usuń task
    del_response = client.delete(
        f"/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert del_response.status_code == 200