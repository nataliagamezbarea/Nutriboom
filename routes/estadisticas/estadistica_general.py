from flask import jsonify
from backend.Modelos.database import db
from sqlalchemy import text
from flask import session
from backend.Modelos.Info_diaria import Info_diaria


def estadistica_general(id_usuario):
    registros = Info_diaria.query.filter(Info_diaria.id_usuario == id_usuario).all()
    if not registros:
        return jsonify({"mensaje": "No hay datos registrados para este usuario"})

    datos = []
    for reg in registros:
        # Cálculo de la masa muscular
        masa_muscular = float(reg.peso) * (1 - float(reg.grasa_corporal) / 100)
        
        datos.append({
            "dia": reg.fecha.strftime("%A"),
            "peso": float(reg.peso),
            "grasa_corporal": float(reg.grasa_corporal),
            "masa_muscular": round(masa_muscular, 2)  # Redondeado a 2 decimales
        })
    
    return jsonify(datos)
