from flask import render_template, session, redirect, url_for
from backend.Modelos.Datos_personales import Datos_personales
from backend.Modelos.Usuario import Usuario

def cuenta():
    if "user" not in session:
        # Si el usuario no está autenticado, redirige al login
        return redirect(url_for("login"))

    user_id = session["user"]
    # Verifica si el usuario tiene datos personales registrados
    datos = Datos_personales.query.filter_by(id_usuario=user_id).first()

    if not datos:
        # Si no tiene datos, redirige a la página de datos personales
        return redirect(url_for("datos_personales"))
    
    # Si tiene datos, redirige a la página principal
    return redirect(url_for("home"))
    user_id = session.get("user")
    if not user_id:
        return redirect(url_for("login"))

    usuario = Usuario.query.filter_by(id_usuario=user_id).first()
    if not usuario:
        return "Usuario no encontrado", 404

    # Le pasamos usuario y marcamos la pestaña activa
    return render_template('usuario_configuracion/cuenta.html',usuario=usuario)
