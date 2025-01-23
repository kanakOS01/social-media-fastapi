import pytest
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    response = authorized_client.get("/posts/")
    assert len(response.json()) == len(test_posts)
    assert response.status_code == 200


def test_unauthorized_user_get_all_posts(client, test_posts):
    response = client.get("/posts/")
    assert response.status_code == 401


def test_get_one_post(authorized_client, test_posts):
    response = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostResponse(**response.json())
    assert post.id == test_posts[0].id
    assert post.title == test_posts[0].title
    assert post.content == test_posts[0].content


def test_unauthorized_user_get_one_post(client, test_posts):
    response = client.get(f"/posts/{test_posts[0].id}")
    assert response.status_code == 401


def test_get_unavailable_post(authorized_client, test_posts):
    response = authorized_client.get("/posts/9999999")
    assert response.status_code == 404


@pytest.mark.parametrize("title, content, published", [
    ("post1", "content1", True),
    ("post2", "content2", True),
    ("post3", "content3", False),
    ("post4", "content4", True),
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    response = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})
    created_post = schemas.PostResponse(**response.json())
    assert response.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner.id == test_user['id']


def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    response = authorized_client.post("/posts/", json={"title": "title", "content": "content"})
    created_post = schemas.PostResponse(**response.json())
    assert response.status_code == 201
    assert created_post.title == "title"
    assert created_post.content == "content"
    assert created_post.published == True
    assert created_post.owner.id == test_user['id']


def test_unauthorized_user_create_post(client):
    response = client.post("/posts/", json={"title": "title", "content": "content"})
    assert response.status_code == 401


def test_delete_post_success(authorized_client, test_user, test_posts):
    response = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert response.status_code == 204


def test_delete_unavailable_post(authorized_client, test_user, test_posts):
    response = authorized_client.delete("/posts/9999999")
    assert response.status_code == 404


def test_delete_other_user_post(authorized_client, test_user, test_user2, test_posts):
    response = authorized_client.delete(f"/posts/{test_posts[4].id}")
    assert response.status_code == 403


def test_unauthorized_user_delete_post(client, test_user, test_posts):
    response = client.delete(f"/posts/{test_posts[0].id}")
    assert response.status_code == 401


def test_update_post(authorized_client, test_user, test_posts):
    response = authorized_client.put(f"/posts/{test_posts[0].id}", json={"title": "new title", "content": "new content", "published": True})
    updated_post = schemas.PostResponse(**response.json())
    assert response.status_code == 200
    assert updated_post.title == "new title"
    assert updated_post.content == "new content"


def test_update_unavailable_post(authorized_client, test_user, test_posts):
    response = authorized_client.put(f"/posts/9999999", json={"title": "new title", "content": "new content", "published": True})
    assert response.status_code == 404


def test_update_other_user_post(authorized_client, test_user, test_user2, test_posts):
    response = authorized_client.put(f"/posts/{test_posts[4].id}", json={"title": "new title", "content": "new content", "published": True})
    assert response.status_code == 403


def test_unauthorized_user_update_post(client, test_user, test_posts):
    response = client.put(f"/posts/{test_posts[0].id}", json={"title": "new title", "content": "new content", "published": True})
    assert response.status_code == 401
