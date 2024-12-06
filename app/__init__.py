from flask import Flask
from mvc_flask import FlaskMVC
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config.from_object("config.Config")

# Initialisez les extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configuration des fichiers
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# Initialisation de FlaskMVC
FlaskMVC(app)

# Ajoutez la migration (si nécessaire)
migrate.init_app(app, db)


