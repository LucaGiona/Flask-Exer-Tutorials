



# Flask Exercises & Tutorials

[Jump to English version](#english-version)

Dies ist eine Sammlung von Projekten und Übungen zur Vertiefung von Flask. Ziel ist es, zentrale Konzepte rund um Routing, Authentifizierung, Datenbankmodelle, APIs und Formularverarbeitung praktisch zu erlernen. Der Fokus liegt auf zwei Projekten:

---

## 1. Microblog Tutorial (nach Miguel Grinberg)

Ein klassisches Lernprojekt, das zentrale Komponenten von Flask behandelt:

- User-Registrierung und Login mit `Flask-Login`
- Profilbearbeitung, letzte Aktivität, About-Me-Feld
- Follower-System mit Explore-Feed
- Postings mit WTForms
- Fehlerbehandlung und Logging
- E-Mail-Versand (Passwort-Reset über SMTP Debug-Server)
- Jinja2-Templates & Sub-Templates (`_post.html`)
- SQLAlchemy ORM mit Migrations via `Flask-Migrate`
- Shell-Kontext für schnelles Testing

Pfad: `Flask_Tutorial_MiguelGrinberg/`

---

## 2. Worktastic API (eigene API für Jobinserate)

Ein modernes API-Projekt mit Fokus auf REST-Architektur:

- User-Registrierung und Authentifizierung (JWT-basiert)
- CRUD-Endpunkte für Jobinserate
- Felder: `title`, `description`, `salary`, `is_published`
- GET-Requests ohne Login, Änderungen nur durch authentifizierte User
- Klare Endpunkte:
  - `GET /jobs`
  - `POST /jobs`
  - `PUT /jobs/<job-id>`
  - `DELETE /jobs/<job-id>/publish`

Pfad: `worktastic-api/`

---

## Ziel dieser Sammlung

- Festigung der zentralen Flask-Konzepte
- Parallel Übung von API-Design und Deployment-Vorbereitung
- Klarer Fortschritt von Web-App zu API-first-Architektur

---

## Diagramme

### 1. Microblog – Entity Relationship Diagram (ERD)

```plaintext
+--------+           +-------+
|  User  | 1       * | Post  |
+--------+-----------+-------+
| id     |           | id    |
| email  |           | body  |
| ...    |           | timestamp
+--------+           | user_id (FK)
                     +-------+

User --- follows --- User (selbstreferenzielle Many-to-Many Beziehung)
```

Zeigt, dass jeder User viele Posts haben kann und anderen Usern folgen kann.

### 2. Worktastic API – API-Flow & Endpoints

```plaintext
[Client] ---> [POST /register] -----------+
         ---> [POST /login] ---> [JWT Token]
         ---> [GET /jobs] (alle, öffentlich)
         ---> [POST /jobs] (mit Token)
         ---> [PUT /jobs/<id>] (nur eigene)
         ---> [DELETE /jobs/<id>/publish] (nur eigene)
```

Zeigt, welche Routen öffentlich zugänglich sind und welche Authentifizierung benötigen.

---

## English version

This repository contains a collection of Flask projects and exercises aimed at strengthening key concepts such as routing, authentication, database modeling, API development, and form handling.

### 1. Microblog Tutorial (based on Miguel Grinberg)

A classic learning project covering core Flask components:

- User registration & login using `Flask-Login`
- Profile editing, last seen tracking, About-Me field
- Follower system with an explore feed
- Post creation via WTForms
- Error handling and logging
- Email functionality (SMTP debug server for password reset)
- Jinja2 templates and sub-templates (`_post.html`)
- SQLAlchemy ORM and migrations via `Flask-Migrate`
- Flask shell context for quick testing

Path: `Flask_Tutorial_MiguelGrinberg/`

### 2. Worktastic API (Job listing API)

A REST-style project focused on building and managing job listings:

- JWT-based user registration and authentication
- CRUD endpoints for job listings
- Fields: `title`, `description`, `salary`, `is_published`
- Public GET requests; authenticated users required for modifications
- Defined endpoints:
  - `GET /jobs`
  - `POST /jobs`
  - `PUT /jobs/<job-id>`
  - `DELETE /jobs/<job-id>/publish`

Path: `worktastic-api/`

### Goals

- Deepen Flask fundamentals
- Practice RESTful API design and deployment structure
- Transition from web applications to API-first architecture

---
