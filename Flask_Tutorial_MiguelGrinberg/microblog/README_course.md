**Flask Microblog Projekt: Lernzusammenfassung & Cheatsheet (Kapitel 1-10)**

---

### 🔧 Projektstruktur & Setup

- `microblog.py`: Einstiegspunkt der App
- `app/`: Enthält Views, Models, Forms, Templates, Mail, Fehlerbehandlung
- `config.py`: Zentrale Konfiguration (SECRET_KEY, DB, Mail etc.)
- Virtuelle Umgebung `.venv` mit Python 3.13
- Installierte Packages (requirements.txt):
  - Flask, Flask-WTF, Flask-Login, Flask-Migrate, Flask-Mail, Flask-SQLAlchemy
  - aiosmtpd (lokaler Mail-Debugserver)

---

### 🔐 Benutzerverwaltung & Authentifizierung

- Registrierung / Login via `WTForms`
- Passwort-Hashing mit `werkzeug.security`
- Login-Verwaltung über `Flask-Login`
  - `UserMixin`, `@login.user_loader`, `login_user`, `logout_user`
- Schutz via `@login_required`
- Weiterleitung nach erfolgreichem Login per `next`-Parameter

---

### ⚖️ Datenbankmodell mit SQLAlchemy + Type Hints

**User**:
```python
id: int
username: str
email: str
password_hash: str
about_me: str | None
last_seen: datetime
posts: list[Post] (Relationship)
followers / following: Secondary-Tabelle + Methoden
```

**Post**:
```python
id: int
body: str (140 Zeichen max)
timestamp: datetime (UTC)
author: User (FK user_id)
```

- Migration via `flask db migrate` / `upgrade`
- User-Methoden: `follow()`, `unfollow()`, `is_following()`, `following_posts()`

---

### 📰 Posts, Feeds & Explore-Ansicht

- Post-Erstellung per Textarea im Index
- `index`: Zeigt Posts von gefolgten Nutzern
- `explore`: Zeigt alle Posts, sortiert nach Timestamp
- Pagination mit `paginate()`
- `_post.html` als Subtemplate zur Anzeige einzelner Posts

---

### 💼 Formulare & WTForms

- `LoginForm`, `RegistrationForm`, `EditProfileForm`, `PostForm`, `ResetPasswordRequestForm`, `ResetPasswordForm`
- Validierung, Labels, Fehleranzeige
- `form.hidden_tag()` für CSRF-Schutz

---

### 🛋️ Profile & Soziale Features

- Eigene Profilseite unter `/user/<username>`
- Editieren von `username` und `about_me`
- Follow/Unfollow per Button und `EmptyForm`
- Anzeige: Anzahl Follower / Following

---

### 📧 Passwort-Reset via Mail (Kap. 10)

- `ResetPasswordRequestForm`: Benutzer sendet Email-Adresse
- `email.py`: Enthält `send_email()` + `send_password_reset_email()`
- Token-Erstellung via `itsdangerous` (Methode im User-Modell)
- Debug-Mailserver via `aiosmtpd` auf Port 8025:
```bash
python3 -m aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025
```
- Emails werden im Terminal als Klartext angezeigt

---

### 🔍 Flask-Shell & Admin Tools

- Shell-Context: Zugriff auf `db`, `User`, `Post` etc.
```python
>>> user = User(username="Test", email="test@example.com")
>>> user.set_password("pass123")
>>> db.session.add(user); db.session.commit()
```
- Benutzer direkt auslesen oder neue Posts erstellen

---

### 🔐 Sicherheit & Fehlerbehandlung

- Fehlerseiten: `404.html`, `500.html`
- Logging via `RotatingFileHandler`
- Email bei kritischen Fehlern (optional)
- CSRF-Schutz per Flask-WTF Standardmechanismus

---

### 🌐 Weitere Features

- Gravatar-Integration
- Zeitstempel: `last_seen` aktualisiert per `@app.before_request`
- Dynamische URLs: Profile, Follow-Buttons, Token-URLs für Reset

---




