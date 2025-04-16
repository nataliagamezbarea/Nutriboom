from flask import render_template, request, redirect, url_for, session
from backend.Modelos.database import db
from backend.Modelos.Ingredientes import Ingredientes
from backend.Modelos.platos import Platos
from math import ceil

TIPOS_PLATO = ["Desayuno", "Almuerzo", "Merienda", "Cena"]

def platos():
    if 'is_admin' not in session:
        return redirect(url_for('login'))

    ingredientes = Ingredientes.query.order_by(Ingredientes.nombre.desc()).all()  
    pagina = request.args.get('page', 1, type=int)
    per_page = 10
    platos_paginated = Platos.query.paginate(page=pagina, per_page=per_page)

    return render_template(
        'platos/platos.html', 
        ingredientes=ingredientes, 
        platos=platos_paginated.items,
        tipos_plato=TIPOS_PLATO,
        current_page=pagina,
        total_pages=ceil(Platos.query.count() / per_page),
        plato_a_editar=None,  
        ingredientes_ids=[]
    )
