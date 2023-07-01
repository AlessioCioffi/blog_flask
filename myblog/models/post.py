from myblog import db
from datetime import datetime


# Crear el modelo de tabla que se transfiere a la base de datos
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    # Relaciónar la tabla post a la de users en su columna id
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(50))
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, author, title, content):
        # Argumentos necesarios para la creación de la instancia
        self.author = author
        self.title = title
        self.content = content

    def __repr__(self):
        return f'Post: {self.title}'
