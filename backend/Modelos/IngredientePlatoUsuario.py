from backend.Modelos.database import db 

class IngredientePlato(db.Model):
    id_plato = db.Column(db.Integer, primary_key=True)
    id_ingrediente = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Decimal(6, 2), nullable=False)
    day = db.Column(db.Enum('Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'))