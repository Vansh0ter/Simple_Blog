import psycopg2
import os
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = FastAPI()


local_dbname=os.getenv("POSTGRES_DB")
db_user= os.getenv("POSTGRES_USER")
db_pass=os.getenv("POSTGRES_PASSWORD")

def get_connection():
	conn = psycopg2.connect(dbname=local_dbname, user=db_user, password=db_pass, host='db', cursor_factory=RealDictCursor)
	return conn



class Post(BaseModel):
	title: str
	content: str

class PostResp(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True

@app.on_event("startup")
def startup():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

@app.get("/posts", response_model=List[PostResp])
def get_posts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM posts ORDER BY id")
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return posts

@app.post("/posts", response_model=PostResp, status_code=201)
def create_post(post: Post):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING id, title, content",
        (post.title, post.content)
    )
    new_post = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return new_post
