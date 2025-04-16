from flask import render_template, request, redirect, session, url_for, flash
from backend.Modelos.Ingredientes import Ingredientes
from backend.Modelos.database import db

def add_ingrediente():
    if 'is_admin' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        grasas_saturadas = request.form['grasas_saturadas']
        grasas_no_saturadas = request.form['grasas_no_saturadas']
        carbohidratos = request.form['carbohidratos']
        azucar = request.form['azucar']
        proteina = request.form['proteina']

        # Validar que los valores numéricos sean correctos
        try:
            grasas_saturadas = float(grasas_saturadas)
            grasas_no_saturadas = float(grasas_no_saturadas)
            carbohidratos = float(carbohidratos)
            azucar = float(azucar)
            proteina = float(proteina)

            if grasas_saturadas < 0 or grasas_no_saturadas < 0 or carbohidratos < 0 or azucar < 0 or proteina < 0:
                flash('Los valores numéricos no pueden ser negativos.', 'error')
                return render_template('add_ingrediente.html')

        except ValueError:
            flash('Por favor, ingrese valores válidos en todos los campos numéricos.', 'error')
            return render_template('add_ingrediente.html')

        # Crear un nuevo ingrediente con los datos del formulario
        nuevo_ingrediente = Ingredientes(
            nombre=nombre,
            grasas_Saturadas=grasas_saturadas,
            grasas_NO_Saturadas=grasas_no_saturadas,
            carbohidratos=carbohidratos,
            azucar=azucar,
            proteina=proteina
        )

        # Agregar el nuevo ingrediente a la base de datos
        db.session.add(nuevo_ingrediente)
        db.session.commit()

        flash('Ingrediente añadido correctamente.', 'success')
        return redirect(url_for('ingredientes'))

    return render_template('add_ingrediente.html')  # Mostrar el formulario para añadir ingredientes
