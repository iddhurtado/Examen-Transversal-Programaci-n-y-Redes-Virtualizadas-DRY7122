from flask import Flask, request
import sqlite3
import hashlib
import os

# Configuración de Flask
app = Flask(__name__)

# Crear base de datos si no existe
if not os.path.exists("usuarios.db"):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE usuarios (nombre TEXT, contrasena TEXT)")
    conn.commit()
    conn.close()

# Ruta para registrar usuarios (solo POST)
@app.route('/registro', methods=['POST'])
def registrar():
    nombre = request.form.get('nombre')
    contrasena = request.form.get('contrasena')
    if not nombre or not contrasena:
        return "Faltan datos", 400

    # Hashear la contraseña
    hash_pass = hashlib.sha256(contrasena.encode()).hexdigest()

    # Guardar en la base de datos
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, contrasena) VALUES (?, ?)", (nombre, hash_pass))
    conn.commit()
    conn.close()

    return f"Usuario {nombre} registrado correctamente."

# Ejecutar en puerto 5800
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800)

