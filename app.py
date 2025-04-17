import os
from flask import Flask
from flask_cors import CORS
from backend.Modelos.database import db, init_db

from routes.home import home  
from routes.login import login
from routes.register import register
from routes.id_usuario import ver_id_usuario
from routes.estadistica import estadistica
from routes.datos_personales import datos_personales
from routes.logout import logout  



from routes.platos import *
from routes.ingredientes import *
from routes.info_diaria import *

app = Flask(__name__)
app.secret_key = os.urandom(24)

CORS(app)

init_db(app)

# Rutas
app.add_url_rule('/', 'home', home)  
app.add_url_rule('/login', 'login', login, methods=["GET", "POST"])
app.add_url_rule('/register', 'register', register, methods=["GET", "POST"])
app.add_url_rule('/ver_id_usuario', 'ver_id_usuario', ver_id_usuario)
app.add_url_rule('/estadistica/<int:id_usuario>', 'estadistica', estadistica)
app.add_url_rule('/datos_personales', 'datos_personales', datos_personales, methods=["GET", "POST"])

app.add_url_rule('/platos', 'platos', platos, methods=["GET", "POST"]) 
app.add_url_rule('/plato/add', 'add_plato', add_plato, methods=["POST"])  
app.add_url_rule('/plato/delete/<int:id_plato>', 'delete_plato', delete_plato, methods=["POST"])  
app.add_url_rule('/plato/update/<int:id_plato>', 'update_plato', update_plato, methods=["GET", "POST"])  
app.add_url_rule('/delete_platos' , 'delete_platos' , delete_platos ,  methods = ['POST'])


app.add_url_rule('/ingredientes', 'ingredientes', ingredientes, methods=["GET", "POST"]) 
app.add_url_rule('/ingrediente/add', 'add_ingrediente', add_ingrediente, methods=["POST"]) 
app.add_url_rule('/ingrediente/update/<int:id_ingrediente>', 'update_ingrediente', update_ingrediente, methods=["GET", "POST"])  
app.add_url_rule('/ingrediente/delete/<int:id_ingrediente>', 'delete_ingrediente', delete_ingrediente, methods=["POST"])  
app.add_url_rule('/delete_ingredientes' , 'delete_ingredientes' , delete_ingredientes ,  methods = ['POST'])

app.add_url_rule('/info_diaria', 'info_diaria', info_diaria, methods=["GET", "POST"]) 
app.add_url_rule('/info_diaria/add', 'add_info_diaria', add_info_diaria, methods=["POST"]) 
app.add_url_rule('/info_diaria/update/<int:id_info_diaria>', 'update_info_diaria', update_info_diaria, methods=["GET", "POST"])  
app.add_url_rule('/info_diaria/delete/<int:id_info_diaria>', 'delete_info_diaria', delete_info_diaria, methods=["POST"])  
app.add_url_rule('/delete_info_diarias' , 'delete_info_diarias' , delete_info_diarias ,  methods = ['POST'])

app.add_url_rule('/cerrar_sesion', 'logout', logout)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)