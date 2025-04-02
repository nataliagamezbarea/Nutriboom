from flask import Flask, render_template, request, redirect, url_for , jsonify
from backend.Modelos.database import db   , init_db
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

init_db(app)


from backend.Modelos.Info_diaria import Info_diaria

@app.route('/estadistica/<int:id_usuario>')
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


@app.route('/')
def home():
    return render_template("SeguimientoNutricional.html", )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)

