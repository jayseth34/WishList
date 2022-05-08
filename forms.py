from flask_wtf import FlaskForm 
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name=StringField('Enter your wishlist: ')
    submit=SubmitField('Add')

class DelForm(FlaskForm):
    id=IntegerField('Id to remove your wishlist')
    submit=SubmitField('Remove wishlist')

class AddOwnerForm(FlaskForm):
    name=StringField('Name of your travel partner: ')
    wished_id=IntegerField('Id of wishlist ')
    submit=SubmitField('Add owner')
