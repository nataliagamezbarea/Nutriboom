from flask import jsonify
from backend.Modelos.database import db
from sqlalchemy import text
from flask import session
from backend.Modelos.Info_diaria import Info_diaria


def estadistica(id_usuario):
    registros = Info_diaria.query.filter(Info_diaria.id_usuario == id_usuario).all()
    if not registros:
        return jsonify({"mensaje": "No hay datos registrados para este usuario"})

    datos = []
    for reg in registros:
        datos.append({
            "dia": reg.fecha.strftime("%A"),
            "peso": float(reg.peso),
            "grasa_corporal": float(reg.grasa_corporal)
        })
    return jsonify(datos)
