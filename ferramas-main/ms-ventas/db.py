from flask_mysqldb import MySQL
from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])

conexion = MySQL(app)

def get_db():
    return conexion