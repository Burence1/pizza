from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..models import User, Pizza,Topping
from flask_login import login_required, current_user
from .. import db
from datetime import datetime
from .forms import AddPizza,SelectPizza

@main.route("/")
@login_required
def index():
  '''
  root/homepage
  '''
  title = "Pomodoro"

  message = "welcome"
  return render_template('index.html',title = title,message=message)


@main.route("/add_pizza/",methods=["GET","POST"])
@login_required
def add_pizza():
  form = AddPizza()
  if form.validate_on_submit():
    pizza=Pizza(name=form.name.data,toppings=form.toppings.data,user=current_user,size=form.size.data)
    print(pizza)
    pizza.save_pizza()

    return redirect(url_for("main.add_pizza"))
  title = "New Pizza"
  return render_template ("add_pizza.html",title=title,form=form)

@main.route("/basic")
def basic():
  return render_template('basic.html')