from backend import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
def __repr__(self):
    return f'<User {self.nombre} {self.apellido}>'
def __init__(self, nombre, apellido, email, password):
    self.nombre = nombre
    self.apellido = apellido
    self.email = email
    self.password = password