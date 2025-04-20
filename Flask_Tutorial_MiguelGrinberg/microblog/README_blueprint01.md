# Flask Microblog – Blueprint Refactoring (`blueprint01`)

This version of the Microblog application implements a complete refactoring using Flask Blueprints to modularize the project structure. It also includes internationalization support for German and Italian, and a simulated AJAX-based translation system.

[German version below](#german-summary)

---

## Table of Contents

- [Blueprint Modules](#blueprint-modules)
- [Translations](#translations)
- [AJAX-Based Translation](#ajax-based-translation)
- [Project Structure](#project-structure)
- [Git Tag](#git-tag)
- [German Summary](#german-summary)

---

## Blueprint Modules

| Blueprint | Path         | Description                                 |
|-----------|--------------|---------------------------------------------|
| `main`    | `app/main/`  | Home page, post creation, profile views     |
| `auth`    | `app/auth/`  | Authentication: login, registration, reset  |
| `errors`  | `app/errors/`| Error handling: 404 and 500 pages           |
| `cli`     | `app/cli.py` | Custom Flask CLI commands (e.g. translations) |

All blueprints are registered in the `create_app()` factory function.

---

## Translations

This version supports two languages:

- German (`de`)
- Italian (`it`)

To update and compile message catalogs:

```bash
flask translate update
flask translate compile
```

Translation files are managed via Flask-Babel in the `app/translations/` directory.

---

## AJAX-Based Translation

This feature simulates live translation of user posts using:

- Python: `app/translate.py`
- JavaScript: `static/js/translate.js`

The translation result is simulated based on the configured language and can be toggled via:

```python
FAKE_TRANSLATION = True
```

AJAX requests are sent to the `/translate` route, which returns JSON-formatted text.

---

## Project Structure

```
app/
├── auth/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   └── email.py
├── errors/
│   ├── __init__.py
│   └── handlers.py
├── main/
│   ├── __init__.py
│   ├── routes.py
│   └── forms.py
├── templates/
│   ├── auth/
│   ├── errors/
│   └── base.html
├── static/
│   └── js/translate.js
├── cli.py
├── translate.py
├── models.py
└── ...
```

---

## Git Tag

This version is tagged as:

```bash
git checkout blueprint01
```

Use this tag as a clean reference point for further development.

---

## German Summary

[Back to top](#table-of-contents)

Diese Version der Microblog-Anwendung wurde vollständig mithilfe von Flask-Blueprints modularisiert. Ziel war es, die Codebasis klar zu strukturieren und Erweiterungen zu erleichtern. Zusätzlich wurde Unterstützung für Mehrsprachigkeit (Deutsch und Italienisch) implementiert sowie eine clientseitige Übersetzungsfunktion mit AJAX simuliert.

### Enthaltene Komponenten

- Strukturierung in `auth`, `main`, `errors`, `cli`
- Mehrsprachigkeit via Flask-Babel
- Simulierte Übersetzungen ohne API-Schlüssel
- Projektstruktur vorbereitet für zukünftige Erweiterungen und APIs

Der aktuelle Entwicklungsstand ist mit folgendem Git-Tag markiert:

```bash
git checkout blueprint01
```

Diese Version kann als Referenz für weitere Änderungen oder neue Features verwendet werden.