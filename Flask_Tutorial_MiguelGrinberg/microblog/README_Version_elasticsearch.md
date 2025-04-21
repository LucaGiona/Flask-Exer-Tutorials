elasticsearch_compat.md
markdown
Kopieren
Bearbeiten
# Elasticsearch Kompatibilitätshinweis

## Problem: `media_type_header_exception` (400 Bad Request)

Beim Arbeiten mit der Python-Bibliothek `elasticsearch` in Version **8.x oder 9.x** kann folgender Fehler auftreten:

elasticsearch.BadRequestError: BadRequestError(400, 'media_type_header_exception', 'Invalid media-type value on headers [Content-Type, Accept]')

pgsql
Kopieren
Bearbeiten

## Ursache

Seit Elasticsearch 8.x müssen HTTP-Header wie `Content-Type` explizit angegeben werden, wenn JSON-Daten an die API gesendet werden. Vorher wurde dies automatisch gehandhabt.

## Lösungen

### ✅ Empfohlene Methode (ab Version 8.x+)

```python
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

es.options(headers={"Content-Type": "application/json"}).index(
    index="my_index",
    id=1,
    document={"text": "this is a test"}
)
📌 Alternative für volle Kontrolle (nicht empfohlen für Einsteiger)
python
Kopieren
Bearbeiten
es.transport.perform_request(
    method="POST",
    path="/my_index/_doc/1",
    headers={"Content-Type": "application/json"},
    body={"text": "this is a test"}
)
🧘‍♂️ Vereinfachung (für Kurs oder Legacy-Code)
Downgrade auf eine kompatible Version (z. B. 7.17.10):

bash
Kopieren
Bearbeiten
pip uninstall elasticsearch
pip install elasticsearch==7.17.10
Dadurch funktionieren ältere Tutorials oder Beispiele ohne Änderungen.

TL;DR
Für moderne Versionen: immer headers={"Content-Type": "application/json"} setzen