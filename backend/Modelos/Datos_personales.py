from app import db 

class Datos_personales(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    altura = db.Column(db.Decimal(5, 2), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.Enum("Masculino","Femenino","Otros"))
    nivel_actividad = db.Column(db.Integer, nullable=False)
    tipo_dieta = db.Column(db.Enum("Subir","Bajar","Mantenerse"))
    calorias_base = db.Column(db.Decimal(8, 2), nullable=False)
    calorias_permitidas = db.Column(db.Decimal(8, 2), nullable=False)