from flask import current_app
from flask_babel import _

def translate(text, source_language, dest_language):
    if current_app.config.get('FAKE_TRANSLATION', False):
        return f"[{dest_language.upper()}] {text}"
    return _('Translation disabled or not available.')
