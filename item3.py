from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

DB = "usuarios.db"

def crear_bd():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        password TEXT
    )
    """)

    usuarios = [
        ("Bradley", "brad123"),
        ("Integrante2", "clave123"),
        ("Integrante3", "python123")
    ]

    for usuario, password in usuarios:
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            c.execute(
                "INSERT INTO usuarios(usuario,password) VALUES(?,?)",
                (usuario, hash_password)
            )
        except:
            pass

    conn.commit()
    conn.close()

crear_bd()

@app.route("/")
def inicio():
    return """
    <h2>Examen Transversal DRY7122</h2>

    <form action="/login" method="post">

    Usuario:<br>
    <input type="text" name="usuario"><br><br>

    Contraseña:<br>
    <input type="password" name="password"><br><br>

    <input type="submit" value="Ingresar">

    </form>
    """

@app.route("/login", methods=["POST"])
def login():

    usuario = request.form["usuario"]
    password = hashlib.sha256(
        request.form["password"].encode()
    ).hexdigest()

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "SELECT * FROM usuarios WHERE usuario=? AND password=?",
        (usuario,password)
    )

    datos = c.fetchone()

    conn.close()

    if datos:
        return "<h1>Acceso Correcto</h1>"
    else:
        return "<h1>Usuario o contraseña incorrectos</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5800)
