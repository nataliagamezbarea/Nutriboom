from flask import render_template, request, redirect, session, url_for
from backend.Modelos.database import db
from backend.Modelos.Usuario import Usuario 
from backend.Modelos.Datos_personales import Datos_personales
import bcrypt

def login():
    if "user" in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        email = request.form["email"]
        contrasena = request.form["contrasena"]

        usuario_encontrado = Usuario.query.filter_by(email=email).first()

        if usuario_encontrado and bcrypt.checkpw(contrasena.encode("utf-8"), usuario_encontrado.contrasena.encode("utf-8")):
            session["user"] = usuario_encontrado.id_usuario
            session["is_admin"] = usuario_encontrado.is_admin

            user_id = session["user"]
            datos = Datos_personales.query.filter_by(id_usuario=user_id).first()

            if not datos:
                return redirect(url_for("datos_personales"))

            return redirect(url_for("home"))

        return render_template("login.html", error="Credenciales incorrectas")

    return render_template("login.html")


def home():
    if "user" not in session:
        return redirect(url_for("login"))
    
    user_id = session["user"]
    print("User ID de la sesión:", user_id)

    datos = Datos_personales.query.filter_by(id_usuario=user_id).first()
    print("Datos encontrados:", datos)

    if not datos:
        return redirect(url_for("datos_personales"))

    return render_template("SeguimientoNutricional.html")
