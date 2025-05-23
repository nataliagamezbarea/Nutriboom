from flask_sqlalchemy import SQLAlchemy

# Creamos la instancia de la base de datos
db = SQLAlchemy()

# Datos del servidor MySQL para natalia
# USER = "root"
# PASSWORD = "1234"
# HOST =   # Puede ser una IP o un dominio
# PORT = "3306"  # Puerto por defecto de MySQL
# DATABASE = "Nutriboom"


# # Datos del servidor MySQL para nosotros
USER = "Antonio"
PASSWORD = "password"
HOST = "localhost"#"172.18.31.159"  # Puede ser una IP o un dominio
PORT = "3306"  # Puerto por defecto de MySQL
DATABASE = "nutriboom"

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
