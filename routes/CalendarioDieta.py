from flask import render_template, redirect, request, url_for, session
from backend.Modelos.Usuario import Usuario
from backend.Modelos.database import db
from sqlalchemy import text
from backend.Modelos.Datos_personales import Datos_personales
from backend.Modelos.platos import Platos
from backend.Modelos.IngredientePlato import IngredientePlato
from backend.Modelos.Ingredientes import Ingredientes
from backend.Modelos.IngredientePlatoUsuario import IngredientePlatoUsuario
from datetime import datetime
# genera una lista de platos, segun su tipo
def generarListPlatosPorTipo(tipo):
    platos = Platos.query.filter(Platos.tipo == tipo).all()
    return platos
# genera los ingredientes del plato en cuestion
def obtenerIngredientesPlato(id_platos):
    ingredientes = []
    ingredientesPlato = IngredientePlato.query.filter(IngredientePlato.id_plato ==id_platos).all()
    for ing in ingredientesPlato:
        ingrediente = Ingredientes.query.filter(Ingredientes.id_ingrediente == ing.id_ingrediente).first()
        ingredientes.append(ingrediente)
    return ingredientes
# funcion que genera modales segun el numero de comidas
def generarModales(numComidas, dia):
    html_modals = ""
    comidas = ["Comida","Cena","Desayuno","Merienda","Almuerzo"]
    # segun el numero de comidas
    for num in range(numComidas):
       tipo = comidas[num]
       platos = generarListPlatosPorTipo(tipo)
       html_modals = html_modals + f"""
      <div id="modalplatos{tipo}" class="modal fade modal-dialog-scrollable" data-bs-backdrop="static" tabindex="-1" aria-labelledby="modalplatostitulo{tipo}" data-bs-keyboard="false">
    
    <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="modalplatostitulo{tipo}">Platos: {tipo}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
"""        
       for plato in platos:
          ingredientePlato = obtenerIngredientesPlato(plato.id_plato)
          html_modals = html_modals + f"""
           <div class="d-flex align-items-start">
           <form method="POST" action="{ url_for('seleccionar_plato',id_plato=plato.id_plato, dia=dia  ) }">
              <img src="{ url_for('static', filename=plato.imagen_plato) }" class="rounded me-3" alt="Imagen" style="width: 80px; height: 80px;">
              <div>
                <h5 class="mb-2">{plato.nombre}</h5>
              <div class="row row-cols-2 g-2 mb-3">
"""         
          for ingrediente in ingredientePlato:
            
            html_modals = html_modals + f"""
            <div class="col"><span class="badge bg-secondary w-100">{ingrediente.nombre}</span></div>
"""
          html_modals = html_modals + f"""
                 </div>
                  <button class="btn btn-sm btn-success">Seleccionar</button>
                  </form>
                </div>
              </div>
"""
       html_modals = html_modals + """      
       </div>
    </div>
  </div>
    </div>
    """
    return html_modals
# genera el arcodeon y sus "tarjetas" segun el numero de comidas
def generarTajetasPlatos(numComidas, dia, user_id):
    comidas = ["Comida","Cena","Desayuno","Merienda","Almuerzo"]
    modales = generarModales(numComidas, dia)
    html_code = """<div class="accordion" id="accordionPanelsStayOpenExampletipo">"""
    #segun el numero de comidas
    for num in range(numComidas):
      tipo = comidas[num]
      plato = (
      Platos.query.join(IngredientePlatoUsuario, IngredientePlatoUsuario.id_plato == Platos.id_plato)
      .filter(IngredientePlatoUsuario.dia==dia, Platos.tipo == tipo)
      .group_by(Platos.id_plato).first()
      )
      if plato:
          IpuLista = IngredientePlatoUsuario.query.filter(IngredientePlatoUsuario.id_usuario == user_id, IngredientePlatoUsuario.dia == dia,IngredientePlatoUsuario.id_plato == plato.id_plato ).all()
          html_code = html_code +  f"""
          
                  <div class="accordion-item{tipo}">
                    <h2 class="accordion-header" id="panelsStayOpen-heading{tipo}">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse{tipo}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{tipo}">
                        {tipo}
                      </button>
                    </h2>
                    <div id="panelsStayOpen-collapse{tipo}" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-heading{tipo}">
                      <div class="accordion-body">
                      <div class="d-flex align-items-start">
                      <img src="{ url_for('static', filename=plato.imagen_plato) }" class="rounded me-3" alt="Imagen" style="width: 80px; height: 80px;">
                        <div>
                        <h5 class="mb-2">{plato.nombre}</h5>
                        <div class="row row-cols-2 g-2 mb-3">
                        """
          # por cada ingredientePlatoUsario
          for ipu in IpuLista:
                        ingrediente = Ingredientes.query.filter(Ingredientes.id_ingrediente == ipu.id_ingrediente).first()
                        html_code = html_code +  f""" 
                        <div class="col"><span class="badge bg-secondary w-100">{ingrediente.nombre}: {ipu.cantidad}g</span></div>
                        """
          html_code = html_code +  f""" 
                        </div>
                        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalplatos{tipo}">
                          Seleccionar {tipo}
                        </button>
                      </div>
                    </div>
                  </div>
                  </div>
                """
      else:
          html_code = html_code +  f"""
          <div class="accordion" id="accordionPanelsStayOpenExampletipo">
                  <div class="accordion-item{tipo}">
                    <h2 class="accordion-header" id="panelsStayOpen-heading{tipo}">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse{tipo}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{tipo}">
                        {tipo}
                      </button>
                    </h2>
                    <div id="panelsStayOpen-collapse{tipo}" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-heading{tipo}">
                      <div class="accordion-body">
                        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalplatos{tipo}">
                          Seleccionar {tipo}
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
                """ 
    return html_code, modales   
# funcion central de calendario dieta
def calendario_dieta(dia="Lunes"): 
    
    if "user" not in session:
        return redirect(url_for("login"))
    
    user_id = session["user"]
    datos = Datos_personales.query.filter_by(id_usuario=user_id).first()

    if not datos:
        return redirect(url_for("datos_personales"))
    

    datos_Usuario = Datos_personales.query.filter_by(id_usuario=user_id).first()

    html, modales = generarTajetasPlatos(int(datos_Usuario.numero_Comidas), dia, user_id)
    
    return render_template("CalendarioDieta.html", day=dia, html=html, modales=modales)

#Funcion que coje el plato y lo asigna al dia y al usuario
def seleccionar_plato(id_plato, dia):
    if "user" not in session:
      return redirect(url_for("login"))
    if request.method == 'POST':
      user_id = int(session["user"])
      datos_Usuario = Datos_personales.query.filter_by(id_usuario=user_id).first()  
      Ingredientes = obtenerIngredientesPlato(id_plato)

      for ing in Ingredientes:
        nuevo_ing_user_plato = IngredientePlatoUsuario(
          id_plato=id_plato,
          id_ingrediente=ing.id_ingrediente,
          id_usuario= int(session["user"]),
          cantidad = 20,
          dia= dia
        )
        db.session.add(nuevo_ing_user_plato)
        db.session.commit()          

    return redirect(url_for("calendario_dieta", dia=dia))


# funcion que nos da los porcentajes segun el tipo de dieta 
#Ahora mismo no esta en funcionamiento
def obtenerPorcentajes(tipo_dieta):
    porcentaje = {}
    match tipo_dieta:
        case "Subir":
            porcentaje = {"proteina": float(0.35), "carbs": float(0.45), "grasas": float(0.20)}
        case "Bajar":
            porcentaje = {"proteina": float(0.45), "carbs": float(0.35), "grasas": float(0.20)}
        case "Mantenerse":
            porcentaje = {"proteina": float(0.30), "carbs": float(0.50), "grasas": float(0.20)}     
    return porcentaje     