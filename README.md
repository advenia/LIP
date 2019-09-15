# LIP

## Server installation

Run these commands in order.

```bash
pip install Django numpy
python manage.py migrate
python manage.py sqlmigrate polls
python manage.py migrate
python manage.py createsuperuser # You can write down your user, email, and password in server/lipserver/credentials, which is in the .gitignore
```

## Google Maps Landmarks Query

```bash
npm install --save express
```

## What We Did
* Scrape database landmarks for database. Google Maps Places API

