# Location-based Information Provider

There are two components: the Android app and the server.

## Android app

The Android app should be compiled using Android Studio or an equivalent setup.

## Server installation

Run these commands in order.

```bash
pip install Django numpy
python manage.py migrate
python manage.py sqlmigrate polls
python manage.py migrate
python manage.py createsuperuser # You can write down your user, email, and password in server/lipserver/credentials, which is in the .gitignore
```
