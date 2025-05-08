from datetime import datetime
import locale
import os
from flask import Flask
from flask_cors import CORS
from backend.Modelos.database import db, init_db
from routes.home import home  
from routes.login import login
from routes.register import register
from routes.id_usuario import ver_id_usuario
from routes.estadistica import estadistica
from routes.CalendarioDieta import calendario_dieta, seleccionar_plato
from routes.datos_personales import datos_personales
from routes.logout import logout  


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
app.add_url_rule('/cerrar_sesion', 'logout', logout)
app.add_url_rule('/calendario_dieta/<dia>', 'calendario_dieta', calendario_dieta, methods=["GET", "POST"])
app.add_url_rule('/calendario_dieta/seleccionar_plato/<int:id_plato>/<dia>', 'seleccionar_plato', seleccionar_plato, methods=["GET", "POST"] )

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)