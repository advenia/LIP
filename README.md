# LIP

## Server installation

Run these commands in order.

```bash
pip install Django numpy
python manage.py migrate
python manage.py sqlmigrate polls 0001
python manage.py migrate
python manage.py createsuperuser # You can write down your user, email, and password in server/lipserver/credentials, which is in the .gitignore
```
