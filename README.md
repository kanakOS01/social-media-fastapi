                                                                                                        # Social Media API with FastAPI

This is a FastAPI-based social media API that includes basic CRUD operations, user authentication, and database migrations using Alembic. It is designed for users to interact with posts, comments, and profiles.

## Features

- User authentication (login/signup)
- CRUD operations for posts and comments
- Database migrations with Alembic
- Fast and secure API built with FastAPI

## Prerequisites

- Python 3.7+
- PostgreSQL (or any supported database)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd social-media-api
```

### 2. Set Up a Virtual Environment

Create a virtual environment using `venv`:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- For **Linux/macOS**:

  ```bash
  source venv/bin/activate
  ```

- For **Windows**:

  ```bash
  venv\Scripts\activate
  ```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Database Configuration

Update your database connection settings in the `.env` file or the `config.py` file. Make sure you have the required database set up (PostgreSQL, for instance) and the correct credentials.

Example `.env`:

```env
DATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your_secret_key
```

### 5. Database Migrations with Alembic

Initialize Alembic and create the migration scripts:

```bash
alembic init alembic
```

This will set up the Alembic folder structure. Now, create a migration script by running:

```bash
alembic revision --autogenerate -m "Initial migration"
```

Apply the migrations to the database:

```bash
alembic upgrade head
```

### 6. Running the Application

You can run the FastAPI application with the following command:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

### 7. Documentation

The FastAPI app automatically generates interactive API documentation using Swagger UI. Visit the following URL to view it:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Directory Structure

```
.
├── alembic/
├── app/
│   ├── api/
│   │   ├── endpoints/
│   │   └── dependencies.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   └── models/
│   │   ├── user.py
│   │   ├── post.py
│   │   └── comment.py
│   ├── main.py
│   └── db.py
├── alembic.ini
├── requirements.txt
└── .env
```

## Example API Endpoints

### User Registration

**POST** `/users/register`

Request body:

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123"
}
```

### User Login

**POST** `/users/login`

Request body:

```json
{
  "username": "john_doe",
  "password": "password123"
}
```

### Create Post

**POST** `/posts/`

Request body:

```json
{
  "title": "My First Post",
  "content": "This is my first post on the platform!"
}
```

### Get All Posts

**GET** `/posts/`

### Create Comment

**POST** `/comments/`

Request body:

```json
{
  "post_id": 1,
  "content": "Great post!"
}
```

## Testing

You can run tests using `pytest`. Make sure to set up a test database in your `.env.test` file if necessary.

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
