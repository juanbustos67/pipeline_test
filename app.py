# Archivo de PRUEBA con una consulta SQL insegura para validar Semgrep
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/usuario")
def usuario():
    nombre = request.args.get("nombre")
    conn = sqlite3.connect("db.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE nombre = '" + nombre + "'")
    return str(cur.fetchall())
