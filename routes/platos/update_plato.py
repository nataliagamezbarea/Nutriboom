from flask import render_template, request, redirect, url_for, session
from backend.Modelos.database import db
from backend.Modelos.Ingredientes import Ingredientes
from backend.Modelos.IngredientePlato import IngredientePlato
from backend.Modelos.platos import Platos
from math import ceil

TIPOS_PLATO = ["Desayuno", "Almuerzo", "Merienda", "Cena"]

def update_plato(id_plato):
    if 'is_admin' not in session:
        return redirect(url_for('login'))

    # Recuperamos el plato a editar
    plato_a_editar = Platos.query.get(id_plato)
    if not plato_a_editar:
        return redirect(url_for('platos'))

    if request.method == 'POST':
        plato_a_editar.nombre = request.form['nombre']
        plato_a_editar.tipo = request.form['tipo']
        nuevos_ingredientes = request.form.getlist('ingredientes')

        # Eliminamos las relaciones actuales
        db.session.query(IngredientePlato).filter_by(id_plato=id_plato).delete()
        # Insertamos las nuevas relaciones
        db.session.bulk_insert_mappings(
            IngredientePlato,
            [{"id_plato": id_plato, "id_ingrediente": int(id_ingrediente)} for id_ingrediente in nuevos_ingredientes]
        )
        db.session.commit()
        return redirect(url_for('platos'))

    # Para mostrar el formulario de edición:
    ingredientes = Ingredientes.query.all()
    # Creamos la lista de ids asociados al plato
    ingredientes_ids = [ingrediente.id_ingrediente for ingrediente in plato_a_editar.ingredientes]

    # También obtenemos la lista completa de platos (por ejemplo, para mantener el listado)
    pagina = request.args.get('page', 1, type=int)
    per_page = 10
    platos_paginated = Platos.query.paginate(page=pagina, per_page=per_page)

    return render_template('platos/platos.html', ingredientes=ingredientes,platos=platos_paginated.items, tipos_plato=TIPOS_PLATO, 
                           current_page=pagina,total_pages=ceil(Platos.query.count() / per_page),
                           plato_a_editar=plato_a_editar, ingredientes_ids=ingredientes_ids   # IDs del plato a editar
    )
