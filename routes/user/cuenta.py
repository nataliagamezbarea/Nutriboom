from flask import render_template, session, redirect, url_for
from backend.Modelos.Usuario import Usuario

def cuenta():
    user_id = session.get("user")
    if not user_id:
        return redirect(url_for("login"))

    usuario = Usuario.query.filter_by(id_usuario=user_id).first()
    if not usuario:
        return "Usuario no encontrado", 404

    # Le pasamos usuario y marcamos la pestaña activa
    return render_template('usuario_configuracion/cuenta.html',usuario=usuario)
