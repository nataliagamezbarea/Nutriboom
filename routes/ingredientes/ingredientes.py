from flask import render_template, request, redirect, url_for, session
from backend.Modelos.database import db
from backend.Modelos.Ingredientes import Ingredientes
from math import ceil

def ingredientes():
    if 'is_admin' not in session:
        return redirect(url_for('login'))

    # Obtener la página actual, con un valor por defecto de 1
    pagina = request.args.get('page', 1, type=int)
    per_page = 10

    # Paginación de los ingredientes
    ingredientes_paginated = Ingredientes.query.order_by(Ingredientes.id_ingrediente.desc()).paginate(page=pagina, per_page=per_page)

    return render_template(
        'ingredientes/ingredientes.html',  # Cambié la ruta para la plantilla a ingredientes
        ingredientes=ingredientes_paginated.items,  # Pasar los ingredientes paginados
        current_page=pagina,
        total_pages=ceil(Ingredientes.query.count() / per_page),  # Calcular el total de páginas
    )
