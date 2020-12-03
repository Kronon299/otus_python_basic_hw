import os

PG_HOST = os.environ["PG_HOST"]

SQLALCHEMY_DATABASE_URI = f"postgres+psycopg2://user:user@{PG_HOST}:5432/task-list"
