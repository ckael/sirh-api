# app/__init__.py
from flask import Flask
from app.extensions import db, migrate,cors
from app.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app,db)
    cors.init_app(app)
    # Enregistrer les routes
    register_routes(app)

    return app
