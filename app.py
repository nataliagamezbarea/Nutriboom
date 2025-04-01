from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Datos del servidor MySQL
USER = "Antonio"
PASSWORD = "password"
HOST = "172.18.11.68"  # Puede ser una IP o un dominio
PORT = "3306"  # Puerto por defecto de MySQL
DATABASE = "nutriboom"

# URI de conexión
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False   

db = SQLAlchemy(app)

class Usuario(db.Model): 
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido1 = db.Column(db.String(50), nullable=True)
    apellido2 = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    contrasena =  db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)


with app.app_context():
    usuarios = Usuario.query.all()
    for usuario in usuarios:
        print(usuario.id_usuario, usuario.nombre, usuario.email)
        
@app.route('/')
def home():
    return render_template("SeguimientoNutricional.html", )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)

