from flask import render_template, redirect, url_for, session
from backend.Modelos.Usuario import Usuario
from backend.Modelos.database import db
from sqlalchemy import text
from backend.Modelos.Datos_personales import Datos_personales
from backend.Modelos.platos import Platos
from backend.Modelos.IngredientePlato import IngredientePlato
from backend.Modelos.IngredientePlatoUsuario import IngredientePlatoUsuario

def generarListPlatosPorTipo(tipo):
    platos = Platos.query.filter(Platos.tipo == tipo).all()
    return platos
def obtenerIngredientesPlato(id_platos):
    ingredientesPlato = IngredientePlato.query.filter(IngredientePlato.id_plato ==id_platos).all()
    return ingredientesPlato

def generarModales(numComidas):
    html_modals = ""
    comidas = ["Comida","Cena","Desayuno","Merienda","Almuerzo"]
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
              <img src="{{ url_for('static', filename='{plato.imagen_plato}') }}" class="rounded me-3" alt="Imagen" style="width: 80px; height: 80px;">
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

        
def generarTajetasPlatos(numComidas, dia, user_id):
    match numComidas:
        case 1:
            modales = generarModales(numComidas)
            html_code = ""
            IptLista = IngredientePlatoUsuario.query.filter(IngredientePlatoUsuario.id_usuario == user_id, IngredientePlatoUsuario.dia == dia).all()
            print(IptLista)
            if IptLista == 0 :
                plato = Platos.query.filter(Platos.id_plato == IptLista[0].id_plato).first()
                print(plato)
            else :
                html_code = html_code +  f"""
                <div class="accordion" id="accordionPanelsStayOpenExample">
                  <div class="accordion-item">
                    <h2 class="accordion-header" id="panelsStayOpen-headingOne">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
                        Comida
                      </button>
                    </h2>
                    <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingOne">
                      <div class="accordion-body">
                        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalplatosComida">
                          Seleccionar Comida
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
                """

                return html_code, modales

        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case default:
            return "<div>Porfavor edite sus datos e indique cuantas comidas hace al dia</div>"

def calendario_dieta(dia): 
    #user_id = int(session["user"])
    user_id = 4 #cambiar al subir los cambios
    datos_Usuario = Datos_personales.query.filter_by(id_usuario=user_id).first()
    platosDia = (
    db.session.query(IngredientePlatoUsuario)
    .join(Platos, IngredientePlatoUsuario.id_plato == Platos.id_plato)
    .filter(IngredientePlatoUsuario.id_usuario == user_id, IngredientePlatoUsuario.dia == dia)
    .add_entity(Platos)  # ← Esto es clave
    .group_by(IngredientePlatoUsuario.id_plato)
    .all()
    )

    html, modales = generarTajetasPlatos(1, dia, user_id)
    return render_template("CalendarioDieta.html", day=dia, html=html, platosDia=platosDia,modales=modales, comidasDiarias=datos_Usuario.numero_Comidas)

def generarComida():
    pass
