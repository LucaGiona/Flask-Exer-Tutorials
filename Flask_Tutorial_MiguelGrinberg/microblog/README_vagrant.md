Flask Production Setup with Gunicorn & Supervisor (Vagrant)

This guide documents a realistic, working deployment setup for a Flask application running in a Vagrant Ubuntu VM, using Gunicorn as the WSGI server and Supervisor for process management.

✅ Prerequisites

Flask project located in /vagrant

Virtual environment in /vagrant/venv

Gunicorn installed inside the virtual environment

Vagrant box based on Ubuntu (e.g. ubuntu/jammy64)

📦 Install Supervisor (in VM)

sudo apt update
sudo apt install supervisor -y

Check:

ls /etc/supervisor/conf.d

⚙️ Create Supervisor config for Flask (Gunicorn)

sudo nano /etc/supervisor/conf.d/microblog.conf

Paste the following:

[program:microblog]
command=/vagrant/venv/bin/gunicorn -b 127.0.0.1:8000 -w 4 microblog:app
directory=/vagrant
user=vagrant
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
environment=PATH="/vagrant/venv/bin",VIRTUAL_ENV="/vagrant/venv"

Save with:

CTRL + O (write)

Enter

CTRL + X (exit)

🔄 Reload Supervisor

sudo supervisorctl reread
sudo supervisorctl update

If already running:

sudo supervisorctl restart microblog

📊 Check status

sudo supervisorctl status

Expected:

microblog     RUNNING   pid 1234, uptime 0:00:30

🧪 Test in browser

Go to:

http://192.168.56.10:8000

(if that's your configured Vagrant IP)

🛑 Stop everything (when needed)

sudo supervisorctl stop microblog
exit          # to leave the VM
vagrant halt  # on your host system

🧠 Notes

Miguel Grinberg's tutorial assumes /home/ubuntu/... – in Vagrant, use /vagrant

Always double-check the path to gunicorn and your project directory

Supervisor gives no nice errors – but the logs will help:

tail -n 20 /var/log/supervisor/supervisord.log

