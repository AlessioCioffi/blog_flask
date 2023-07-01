from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crear la app
app = Flask(__name__)

# Configurar la app en produción o desarrollo
app.config.from_object('config.DevelopmentConfig')

# Relación con base de datos
db = SQLAlchemy(app)

'''
Importar lo modulos y paquetes en manera ordenada para
no encontrar errorer de dependencia circular'''

from myblog.views.auth import auth
app.register_blueprint(auth)

from myblog.views.blog import blog
app.register_blueprint(blog)


with app.app_context():
    db.create_all()

