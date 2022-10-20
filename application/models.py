#Designing the database
from operator import truediv
from application import db

#Creating a dataset class for the duel monster type.
class MonsterType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30))
    
#Creating a dataset class for the duel monster name. 
class MonsterName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    stars = db.Column(db.Interger)
    fk_typeid = db.Column(db.Integer, db.ForeignKey("MonsterType.id"))
    