# Anleitung zur Erstellung einer Flask-API mit SQLAlchemy
Nach eine m Kurs von Jannick Leismann @ programmieren-starten.de

(03/25 jobs angelegt zwischen id9 und id11)

## 1. Einführung in das Model-Konzept
- Ein **Model** repräsentiert eine Klasse in einer Datenbank.  
- Beispiele für Modelle sind `User` und `Post`.  
- Eine **Entität** ist eine einzelne Instanz eines Modells (z. B. ein einzelner Nutzer).

---

## 2. Erstellen der Verzeichnisstruktur
### Schritte:
✅ Erstelle die Verzeichnisse und Dateien:
- `models/` (als Python-Package)
- `resources/`
- `job.py` (für das Job-Modell)

Implementiere die Klasse `Job` mit einer `__init__`-Methode:
- `id` wird automatisch generiert.
- `title`, `description` und `salary` werden als Parameter übergeben.

---

## 3. Implementierung des Job-Modells
### In-Memory-Speicherung (vor der Datenbank-Anbindung)
```python
job_list = []

# Helfermethode zum Generieren einer neuen ID
def get_last_id():
    last_job = 1
    if job_list:
        last_job = job_list[-1].id + 1
    return last_job
```

### Job-Klasse mit `@property` für die Datenrückgabe
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

## 4. Implementierung der API mit Flask-RESTful
Erstelle die Datei `resources/job.py`:

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

## 5. API-Routen in `app.py` registrieren
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

## 6. Arbeiten mit einzelnen Jobs (GET, PUT, DELETE)
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

## 7. PostgreSQL-Anbindung mit SQLAlchemy
### Datenbank in `pgAdmin` erstellen
1. Logge dich in `pgAdmin` ein oder erstelle ein neues Konto.
2. Erstelle eine neue Datenbank mit dem Namen `worktastic`.

### Abhängigkeiten in `requirements.txt` hinzufügen
```
psycopg2-binary==2.9.3  # Datenbanktreiber
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
werkzeug==2.2.3  # Fix für Flask 2.0.2
passlib==1.7.4  # Passwort-Hashing
```

---

## 8. JWT-Authentifizierung und Token-Erneuerung
### JWT-Konfiguration in `config.py`
```python
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://Luca:root@localhost/worktastic"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "our-secret-key"
    JWT_ERROR_MESSAGE_KEY = "message"
```

### JWT-Manager in `extensions.py` initialisieren
```python
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()
```

---

## 9. Token-Ressourcen für Authentifizierung
### Neue Datei `resources/token.py` erstellen
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
            return {"message": "Login-Daten sind nicht korrekt"}, HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=str(user.id), fresh=True)
        refresh_token = create_refresh_token(identity=str(user.id))

        return {"access_token": access_token, "refresh_token": refresh_token}, HTTPStatus.OK
```
## 10. Access Token Refresh
```python
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": access_token}, HTTPStatus.OK
```

### Endpunkte in `app.py` registrieren
```python
from resources.token import TokenResource, RefreshResource

api.add_resource(TokenResource, "/token")
api.add_resource(RefreshResource, "/refresh")
```

---

## 11. JWT-Schutz für Job-Ressourcen
```python
from flask_jwt_extended import jwt_required, get_jwt_identity

class JobListResource(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        job = Job(
            title=data["title"],
            description=data["description"],
            salary=data["salary"]
        )
        user_id = get_jwt_identity()
        job.user_id = user_id
        job.save()
        return job.data, HTTPStatus.CREATED
```

---

## Fazit
✅ Die API ist jetzt mit **JWT-Authentifizierung** gesichert.  
✅ **Nur authentifizierte Nutzer** können Jobs erstellen oder bearbeiten.  
✅ **Refresh Tokens** ermöglichen es, ein Access Token zu erneuern.  

**Nächster Schritt:** API testen mit **Postman** oder ein Frontend anbinden! 🚀
