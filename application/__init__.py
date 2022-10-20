from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Creating a flask object & rendering the templates folder.
app = Flask(__name__, template_folder="templates")

#Sets uo the database via SQLAlchemy sqlite.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Yugioh'

db = SQLAlchemy(app)

# imports the routes.py from via the application folder. 
from application import routes