from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Load models
from .models.carModel import (Car)

# Load Controllers
from .controllers import carController

# Without migration
# @app.before_first_request
# def create_table():
#     db.create_all()

# Run server
if __name__ == '__main__':
    app.run()
