import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app import models, schemas
from app.config import settings
from app.database import get_db
from app.oauth2 import create_access_token
from app import models


# setup use of a test database for testing and override get_db dependency
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOSTNAME}:{settings.DB_PORT}/test_{settings.DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(autoflush=False, bind=engine)


@pytest.fixture
def session():
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data = {"email": "mail@mail.com", "password": "password"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    new_user = response.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def test_user2(client):
    user_data = {"email": "mail2@mail.com", "password": "password"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    new_user = response.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client


@pytest.fixture
def test_posts(test_user, test_user2, session):
    posts_data = [
        {
            "title": "Learning JavaScript",
            "content": "The basics of JavaScript and how to get started.",
            "owner_id": test_user['id']
        },
        {
            "title": "Gardening Tips for Beginners",
            "content": "How to start your own garden and keep plants healthy.",
            "owner_id": test_user['id']
        },
        {
            "title": "Exploring Quantum Computing",
            "content": "An introduction to quantum computers and their applications.",
            "owner_id": test_user['id']
        },
        {
            "title": "The Joy of Reading",
            "content": "Why reading books can improve your mental health and creativity.",
            "owner_id": test_user['id']
        },
        {
            "title": "Cooking Quick Meals",
            "content": "Simple recipes for delicious meals in under 30 minutes.",
            "owner_id": test_user2['id']
        },
    ]
    
    def create_post_model(post):
        return models.Post(**post)
    
    posts = list(map(create_post_model, posts_data))
    session.add_all(posts)
    session.commit()

    posts = session.query(models.Post).all()
    return posts