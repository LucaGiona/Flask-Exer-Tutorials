

✅ Du willst das **in Postman machen**, basierend auf deiner API.

---

## 📬 Beispiel: `POST /jobs` in Postman

### 🔐 Voraussetzung:
Du musst **eingeloggt sein** und ein **JWT Access Token** haben → sonst bekommst du `401 Unauthorized`.

---

## 📦 Schritt-für-Schritt in Postman

### 1. **Zuerst: Access Token holen**

- **POST** `http://127.0.0.1:5000/token`
- Body → raw → JSON:
```json
{
  "username": "luca@internet.com",
  "password": "1234"
}
```
- Antwort:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs..."
}
```

---

### 2. **Dann: POST /jobs**

- **POST** `http://127.0.0.1:5000/jobs`
- Tab: **Headers**
  ```
  Key: Authorization
  Value: Bearer eyJhbGciOiJIUzI1NiIs...     ← Dein Access Token
  ```

- Tab: **Body → raw → JSON**

```json
{
  "title": "Junior Python Developer",
  "description": "Hilf uns bei der API-Entwicklung",
  "salary": 45000
}
```

→ **Senden**

---

### ✅ Ergebnis:

Antwort sollte sein:

```json
{
  "id": 1,
  "title": "Junior Python Developer",
  "description": "Hilf uns bei der API-Entwicklung",
  "salary": 45000,
  "is_published": false
}
```

(oder je nachdem, wie dein `Job.data`-Property aussieht)

---


Alles klar – du bist **gerade in Postman** und siehst z. B.:

```
{{base_url}}/itoken
```

Dann bist du wahrscheinlich in einer **Postman-Collection mit Umgebungsvariablen** – und `{{base_url}}` ist **nicht aufgelöst**, also der Request schlägt fehl oder ist verwirrend.

---

## 🔍 Was bedeutet `{{base_url}}`?

Das ist eine **Umgebungsvariable in Postman**, die als Platzhalter für deine API-Basis-URL gedacht ist, z. B.:

```txt
base_url = http://127.0.0.1:5000
```

---

## ✅ Lösung: Setze `base_url` in Postman

### Schritt-für-Schritt:

1. In Postman oben rechts auf das ⚙️-Icon neben „No Environment“ klicken → `Manage Environments`

2. Erstelle ein neues Environment, z. B. **„Worktastic Local“**

3. Füge die Variable hinzu:

| Key       | Value                   |
|-----------|-------------------------|
| base_url  | `http://127.0.0.1:5000` |

4. Speichern ✅

5. Danach: Wähle oben im Dropdown dein Environment:  
   `🌐 Worktastic Local`

6. Jetzt funktioniert dein Aufruf wie:

```
POST {{base_url}}/token
→ wird zu → POST http://127.0.0.1:5000/token
```

---

## ❓Was ist `/itoken`?

Wenn du wirklich `/itoken` meinst (statt `/token`) – dann ist das vielleicht ein Tippfehler oder ein anderer Endpunkt. Prüfe zur Sicherheit:

- Ist dein Endpoint in `app.py` wirklich so registriert?
  ```python
  api.add_resource(TokenResource, "/token")
  ```

- Oder heißt er dort `"/itoken"`?

---

Wenn du willst, kann ich dir in 2 Minuten die ganze Collection „reparieren“ und dir mit `{{base_url}}` + Token-Verwendung vorkonfigurieren.  
Willst du das?





