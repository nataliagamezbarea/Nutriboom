from backend.Modelos.database import db 

class Ingredientes(db.Model):
    id_ingrediente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    grasas_Saturadas = db.Column(db.Decimal(5, 2), nullable=False)
    grasas_NO_Saturadas = db.Column(db.Decimal(5, 2), nullable=False)
    carbohidratos = db.Column(db.Decimal(5, 2), nullable=False)
    azucar = db.Column(db.Decimal(5, 2), nullable=False)
    proteina = db.Column(db.Decimal(5, 2), nullable=False)