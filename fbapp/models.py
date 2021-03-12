from flask_sqlalchemy import SQLAlchemy
import logging as lg

from .views import app

# Create database connection object
db = SQLAlchemy(app)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200), nullable=False)
    auteur = db.Column(db.String(200), nullable=False)
    com = db.Column(db.String(200), nullable=True)

    def __init__(self, nom, auteur, com):
        self.nom = nom
        self.auteur = auteur
        self.com = com

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Games("Undertale", "Toby Fox et équipe", "https://undertale.com"))
    db.session.add(Games("Deltarune", "Toby Fox et équipe", "https://www.deltarune.com"))
    db.session.commit()
    lg.warning('Base de données initialisée !')

db.create_all()