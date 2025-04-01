from app import db 

class IngredientePlato(db.Model):
    id_plato = db.Column(db.Integer, primary_key=True)
    id_ingrediente = db.Column(db.Integer, primary_key=True)