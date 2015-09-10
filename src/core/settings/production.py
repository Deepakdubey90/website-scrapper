import os
import json
import dj_database_url

SECRET_KEY = '(6q#6=%xkx4obr4k_4fo*j*(**f$$vd%xtr2bo9bg2_b$cl11='

DEBUG = False

connection = dj_database_url.parse(os.environ.get("DATABASE_URL"))
connection.update({
    'CONN_MAX_AGE': 600,
})
DATABASES = {
    "default": connection,
}

ALLOWED_HOSTS = [os.environ.get("HOST", "*"), ]
