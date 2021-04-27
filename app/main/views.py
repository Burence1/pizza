from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..models import User, Pizza,Topping
from flask_login import login_required, current_user
from .. import db
from datetime import datetime

@main.route("/")
@login_required
def index():
  '''
  root/homepage
  '''
  title = "Pomodoro"

  message = "welcome"
  return render_template('index.html',title = title,message=message)


@main.route("/add_pizza")
def add_pizza():
  