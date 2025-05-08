from flask import render_template, request, redirect, url_for, session
from backend.Modelos.Datos_personales import Datos_personales
from backend.Modelos.database import db

def datos_personales():
    if "user" not in session:
        return redirect(url_for("login"))

    user_id = int(session["user"]) 

    if request.method == "POST":
        altura = float(request.form.get("altura", 0))
        edad = int(request.form.get("edad", 0))
        genero = request.form.get("genero", "Masculino")
        nivel_actividad = int(request.form.get("nivel_actividad", 1))
        tipo_dieta = request.form.get("tipo_dieta", "Mantenerse")
        calorias_base = float(request.form.get("calorias_base", 0))
        calorias_permitidas = float(request.form.get("calorias_permitidas", 0))
        numero_Comidas = int(request.form.get("numero_Comidas", 1))
        datos = Datos_personales.query.filter_by(id_usuario=user_id).first()

        if not datos:
            nuevo_dato = Datos_personales(
                id_usuario=user_id, 
                altura=altura, 
                edad=edad, 
                genero=genero, 
                nivel_actividad=nivel_actividad, 
                tipo_dieta=tipo_dieta, 
                calorias_base=calorias_base, 
                calorias_permitidas=calorias_permitidas , 
                numero_Comidas = numero_Comidas
            )
            db.session.add(nuevo_dato)
        else:
            datos.altura = altura
            datos.edad = edad
            datos.genero = genero
            datos.nivel_actividad = nivel_actividad
            datos.tipo_dieta = tipo_dieta
            datos.calorias_base = calorias_base
            datos.calorias_permitidas = calorias_permitidas
            datos.numero_Comidas = numero_Comidas

        db.session.commit()

        return redirect(url_for("home"))  

    datos = Datos_personales.query.filter_by(id_usuario=user_id).first()
    
    if datos:
        return render_template("datos_personales.html", datos=datos)

    return render_template("datos_personales.html", mensaje="No tienes datos registrados.")
