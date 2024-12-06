import os

class Config:
    UPLOADED_PHOTOS_DEST = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app\\public\\uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limite de 16 Mo
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/fiche_db'