import os
class Config:
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://root:root@db:3306/usuarios_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
