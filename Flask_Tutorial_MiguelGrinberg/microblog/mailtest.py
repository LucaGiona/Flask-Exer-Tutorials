from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='localhost',
    MAIL_PORT=8025,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=None,
    MAIL_PASSWORD=None,
    MAIL_DEFAULT_SENDER='debug@example.com'
)

mail = Mail(app)

@app.route('/')
def index():
    msg = Message(subject='Test Subject',
                  recipients=['debug@example.com'],
                  body='This is a test email body.',
                  html='<h1>This is HTML</h1>')
    mail.send(msg)
    return 'Mail sent!'

if __name__ == '__main__':
    app.run(port=5001)
