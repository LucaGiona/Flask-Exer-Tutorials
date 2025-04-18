# Guide to Creating a Flask API with SQLAlchemy
After acourse of Jannick Leismann @ programmieren-starten.de

(03/25 jobs between id9 and  id11 are in json - as prefile)

## 1. Introduction to the Model Concept
- A **model** represents a class in a database.  
- Examples of models include `User` and `Post`.  
- An **entity** is a single instance of a model (e.g., a single user).

---

## 2. Creating the Directory Structure
### Steps:
✅ Create the following directories and files:
- `models/` (as a Python package)
- `resources/`
- `job.py` (for the Job model)

Implement the `Job` class with an `__init__` method:
- `id` will be generated automatically.
- `title`, `description`, and `salary` are passed as parameters.

---

## 3. Implementing the Job Model
### In-Memory Storage (Before Database Integration)
```python
job_list = []

# Helper function to generate a new ID
def get_last_id():
    last_job = 1
    if job_list:
        last_job = job_list[-1].id + 1
    return last_job
```

### Job Class with `@property` for Data Representation
```python
class Job:
    def __init__(self, title, description, salary):
        self.id = get_last_id()
        self.title = title
        self.description = description
        self.salary = salary

    @property
    def data(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "salary": self.salary
        }
```

---

## 4. Implementing the API with Flask-RESTful
Create the file `resources/job.py`:

```python
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.job import Job, job_list

class JobListResource(Resource):
    def get(self):
        data = [job.data for job in job_list if job.is_published]
        return {"data": data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        job = Job(
            title=data["title"],
            description=data["description"],
            salary=data["salary"]
        )
        job_list.append(job)
        return job.data, HTTPStatus.CREATED
```

---

## 5. Registering API Routes in `app.py`
```python
from flask import Flask
from flask_restful import Api
from resources.job import JobListResource, JobResource

app = Flask(__name__)
api = Api(app)

api.add_resource(JobListResource, "/jobs")
api.add_resource(JobResource, "/jobs/<int:job_id>")
```

---

## 6. Managing Individual Jobs (GET, PUT, DELETE)
```python
class JobResource(Resource):
    def get(self, job_id):
        job = next((job for job in job_list if job.id == job_id and job.is_published), None)
        if job is None:
            return {"message": "Job not found"}, HTTPStatus.NOT_FOUND
        return job.data, HTTPStatus.OK

    def put(self, job_id):
        data = request.get_json()
        job = next((job for job in job_list if job.id == job_id), None)
        if job is None:
            return {"message": "Job not found"}, HTTPStatus.NOT_FOUND
        job.title = data["title"]
        job.description = data["description"]
        job.salary = data["salary"]
        return job.data, HTTPStatus.OK

    def delete(self, job_id):
        job = next((job for job in job_list if job.id == job_id), None)
        if job is None:
            return {"message": "Job not found"}, HTTPStatus.NOT_FOUND
        job_list.remove(job)
        return {}, HTTPStatus.NO_CONTENT
```

---

## 7. PostgreSQL Integration with SQLAlchemy
### Creating the Database in `pgAdmin`
1. Log into `pgAdmin` or create a new account.
2. Create a new database named `worktastic`.

### Add Dependencies to `requirements.txt`
```
psycopg2-binary==2.9.3  # Database driver
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
werkzeug==2.2.3  # Fix for Flask 2.0.2
passlib==1.7.4  # Password hashing
```

---

## 8. JWT Authentication and Token Refresh
### JWT Configuration in `config.py`
```python
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://Luca:root@localhost/worktastic"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "our-secret-key"
    JWT_ERROR_MESSAGE_KEY = "message"
```

### Initializing JWT Manager in `extensions.py`
```python
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()
```

---

## 9. Token Resources for Authentication
### Create a new file `resources/token.py`
```python
from flask import request
from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from models.user import User

class TokenResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.get_by_username(username)

        if not user or not User.verify_password(password, user.password):
            return {"message": "Login data is incorrect"}, HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=str(user.id), fresh=True)
        refresh_token = create_refresh_token(identity=str(user.id))

        return {"access_token": access_token, "refresh_token": refresh_token}, HTTPStatus.OK
```

---

## Conclusion
✅ The API is now secured with **JWT authentication**.  
✅ **Only authenticated users** can create or modify jobs.  
✅ **Refresh Tokens** allow renewing access tokens.  

**Next Step:** Test the API using **Postman** or connect it to a frontend! 🚀
