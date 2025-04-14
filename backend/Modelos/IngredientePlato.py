from backend.Modelos.database import db 


class IngredientePlato(db.Model):
    __tablename__ = 'ingredientePlato'
    id_plato = db.Column(db.Integer, primary_key=True)
    id_ingrediente = db.Column(db.Integer, primary_key=True)
