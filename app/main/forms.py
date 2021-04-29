from wtforms import SelectField,TextField,StringField,SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class AddPizza(FlaskForm):
  name = TextField("Add pizza",validators=[Required()])
  toppings=StringField("Add toppings",validators=[Required()])
  size=SelectField("Add size",choices=[("small size","small size"),("medium size","medium size"),("large size","large size")],validators=[Required()])
  submit=SubmitField("Add Pizza")

class SelectPizza(FlaskForm):
  name=TextField("Choose pizza",validators=[Required()])
  toppings=QuerySelectField("Select fav topping",query_factory=lambda:Topping.query.all())
  size=SelectField("select size",validators=[Required()])
  submit=SubmitField("Submit")