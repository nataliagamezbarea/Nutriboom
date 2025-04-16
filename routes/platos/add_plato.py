from flask import render_template, request, redirect, url_for, session
from backend.Modelos.database import db
from backend.Modelos.Ingredientes import Ingredientes
from backend.Modelos.IngredientePlato import IngredientePlato
from backend.Modelos.platos import Platos
from math import ceil

TIPOS_PLATO = ["Desayuno", "Almuerzo", "Merienda", "Cena"]

def add_plato():
    if 'is_admin' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        ingredientes = request.form.getlist('ingredientes')

        nuevo_plato = Platos(nombre=nombre, tipo=tipo)
        db.session.add(nuevo_plato)
        db.session.commit()
        # El método de SQLAlchemy permite insertar múltiples registros de manera eficiente.
        # Para cada id_ingrediente en la lista nuevos_ingredientes:
        #   - Asociamos el id_plato con el id_ingrediente
        #   - Creamos un diccionario con ambos valores y lo preparamos para la inserción en la tabla IngredientePlato
        # La función bulk_insert_mappings insertará todas estas relaciones en la base de datos de una sola vez. A diferencia del add permite al mismo tiempo insertarlos
        db.session.bulk_insert_mappings(IngredientePlato, [{"id_plato": nuevo_plato.id_plato, "id_ingrediente": int(id_ingrediente)} for id_ingrediente in ingredientes])
        db.session.commit()
        return redirect(url_for('platos'))

    ingredientes = Ingredientes.query.all()
    return render_template('add_plato.html', ingredientes=ingredientes, tipos_plato=TIPOS_PLATO)
