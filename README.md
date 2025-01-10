# Social Media API with FastAPI

This is a FastAPI-based social media API that includes basic CRUD operations, user authentication, schema validation, and database migrations using Alembic. It is designed for users to interact with posts, comments, and profiles.

## Features

- User authentication (login/signup)
- CRUD operations for posts and comments
- Database migrations with Alembic
- Fast and secure API built with FastAPI

## Prerequisites

- Python 3.8+
- PostgreSQL

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/kanakOS01/social-media-fastapi.git
cd social-media-fastapi
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Database Configuration

Update your database connection settings in the `.env` file.
Create secret key using `openssl rand -hex 32`
```
DB_HOSTNAME=
DB_PORT=
DB_PASSWORD=
DB_USERNAME=
DB_NAME=
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=
```

### 5. Database Migrations with Alembic

Create a database.
Apply latest alembic revision.

```bash
alembic upgrade head
```

### 6. Running the Application

You can run the FastAPI application with the following command:

```bash
fastapi dev --app app
```

The API will be available at `http://localhost:8000`.

### 7. Documentation

The FastAPI app automatically generates interactive API documentation using Swagger UI. Visit the following URL to view it:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Directory Structure

```
.
├── alembic
├── alembic.ini
├── app
│   ├── routers
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── oauth2.py
│   ├── schemas.py
│   └── utils.py
├── README.md
├── requirements.txt
└── .env
```
