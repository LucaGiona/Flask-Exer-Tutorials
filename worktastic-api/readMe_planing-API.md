# Planung der API – Some Pre-Notes

[For English, see below](#workstatic-api-functions)

## Funktionen der Workstatic API

- Nutzer können sich registrieren.
- Nutzer können sich einloggen.
- Eingeloggte Nutzer können Jobinserate erstellen, bearbeiten und entfernen  
  (natürlich nur die eigenen Inserate).
- Nicht authentifizierte Nutzer können Inserate lesen (`GET`).

### Erforderliche Felder für Jobinserate:

- `id` (Primary Key) → Fortlaufende ID (bleibt bestehen, auch wenn das Inserat gelöscht wird)
- `title` (Titel)
- `description` (Beschreibung)
- `salary` (Gehalt)
- `is_published` (Veröffentlicht/Entwurf)

### API-Endpunkte für Jobinserate:

- `/jobs` [`GET`, `POST`]
- `/jobs/<job-id>` [`GET`, `PUT`]
- `/jobs/<job-id>/publish` [`PUT`, `DELETE`]

---

## Workstatic API Functions

- Users can register.
- Users can log in.
- Logged-in users can create, edit, and delete job listings  
  (but only their own listings).
- Non-authenticated users can read listings (`GET`).

### Required Fields for Job Listings:

- `id` (Primary Key) → Sequential ID (persists even after deletion)
- `title`
- `description`
- `salary`
- `is_published` (Published/Draft)

### API Endpoints for Job Listings:

- `/jobs` [`GET`, `POST`]
- `/jobs/<job-id>` [`GET`, `PUT`]
- `/jobs/<job-id>/publish` [`PUT`, `DELETE`]
