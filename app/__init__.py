"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chab8bak728r8808t55g-a.oregon-postgres.render.com",
        database="todo_s9qc",
        user="root",
        password="B3XJaRhZvqmIkcUcfiOY41IcK2wsT4A7")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
