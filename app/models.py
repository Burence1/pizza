from . import db
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
  __tablename__= 'users'

  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(30))
  email = db.Column(db.String(255))
  password_hash=db.Column(db.String(255))
  pizzas=db.relationship('Pizza',backref='user',lazy='dynamic')
  toppings=db.relationship('Topping',backref='user',lazy='dynamic')

  @property
  def password(self):
    raise AttributeError("Canniot read password attribute")

  @password.setter
  def password(self,password):
    self.password_hash = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.password_hash,password)


  def __repr__(self):
    return f"User {self.username}"

class Pizza(db.Model):
  __tablename__= 'pizzas'

  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(255))
  size = db.Column(db.String(255))
  user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
  toppings=db.relationship('Topping',backref='pizza',lazy='dynamic')

  def save_pizza(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_pizzas(cls,id):
    pizzas=Pizza.query.filter_by(user_id=id).all()
    
    return pizzas

  def __repr__(self):
    return f"{self.name}"

class Topping(db.Model):
    __tablename__= 'toppings'

    id = db.Column(db.Integer,primary_key=True)
    add_topping=db.Column(db.String(255))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    pizza_id=db.Column(db.Integer,db.ForeignKey('pizzas.id'))

    def save_toppings(self):
      db.session.add(self)
      db.session.commit()

    @classmethod
    def get_toppings(cls,id):
      toppings=Topping.query.filter_by(pizza_id=id).all()
      return toppings
    
    def __repr__(self):
      return f"{self.add_topping}"