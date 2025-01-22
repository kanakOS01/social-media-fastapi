import pytest
import jwt

from app import schemas
from app.config import settings


def test_root(client):
    response = client.get("/")
    assert response.json().get("message") == "Hello World"
    assert response.status_code == 200


def test_create_user(client):
    response = client.post("/users/", json={"email": "mail@mail.com", "password": "password"})
    new_user = schemas.UserResponse(**response.json())
    assert new_user.email == "mail@mail.com"
    assert response.status_code == 201


def test_login_user(client, test_user):
    response = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_token = schemas.Token(**response.json())
    payload = jwt.decode(login_token.access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_token.token_type == "bearer"
    assert response.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ("wrongmail@mail.com", "password", 403),
    ("mail@mail.com", "wrongpassword", 403),
    ("wrongmail@mail.com", "wrongpassword", 403),
    (None, "password", 403),
    ("mail@mail.com", None, 403),
])
def test_incorrect_login(client, test_user, email, password, status_code):
    response = client.post("/login", data={"username": email, "password": password})
    assert response.status_code == status_code