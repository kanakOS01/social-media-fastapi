import psycopg2
import time
from psycopg2.extras import RealDictCursor
from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='social-media-db', user='postgres', password='kin@fed01', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connected successfully")
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"id": 1, "title": "Post 1", "content": "This is the content of post 1"},
    {"id": 2, "title": "Post 2", "content": "This is the content of post 2"},
]

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", 
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    try:
        post = my_posts[id - 1]
    except Exception:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"error": "Post not found"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    return {"data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    try:
        my_posts.pop(id - 1)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    try:
        my_posts[id - 1] = post.model_dump()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    return {"data": my_posts[id - 1]}
