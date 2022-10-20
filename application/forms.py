#Linking the database via routes and creating the input forms
from flask_wtf import Flaskform
from wtforms import StringField, SubmitField, SelectField, IntegerField
from application import MonsterName, MonsterType

#Creating a class object for the duel monster card name, i.e. Dark Magician, Blue-Eyes White Dragon, etc.
class Monsterform(Flaskform):
    name = StringField("Duel Monster Name")
    stars = StringField("Duel Monster Star Level")
    fk_typeid = IntegerField("Type ID")
    submit = SubmitField("Submit")

#Creating a class object for the duel monster type, i.e. Spellcaster, Dragon, etc.  
class TypeForm(Flaskform):
    type = StringField("Duel Monster Type")
    submit = SubmitField("Submit")
