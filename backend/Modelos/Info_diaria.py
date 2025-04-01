from app import db 

class Info_diaria(db.Model):
    id_info_diaria = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    peso = db.Column(db.Decimal(5, 2), nullable=False)
    grasa_corporal = db.Column(db.Decimal(5, 2), nullable=False)
