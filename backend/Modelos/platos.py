from backend.Modelos.database import db 

class Platos(db.Model):
    __tablename__ = 'platos'
    id_plato = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.Enum("Desayuno","Comida","Merienda", "Cena"))