from flask import render_template, redirect, url_for, session
from backend.Modelos.Datos_personales import Datos_personales
from backend.Modelos.database import db

def home():
    if "user" not in session:
        return redirect(url_for("login"))
    
    user_id = session["user"]

    datos = Datos_personales.query.filter_by(id_usuario=user_id).first()

    if not datos:
        return redirect(url_for("datos_personales"))

    return render_template("SeguimientoNutricional.html")
