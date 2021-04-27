from .. import db
from flask import redirect,render_template,flash,url_for,request
from . import auth
from app.models import User
from flask_login import login_user,logout_user,login_required
from .forms import Registration,LoginForm

@auth.route('/register',methods=["GET","POST"])
def register():
  form=Registration()
  if form.validate_on_submit():
    user=User(username=form.username.data,email=form.email.data,password=form.password.data)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auth.login"))

  return render_template("auth/register.html",registration_form=form)


@auth.route('/login',methods=["GET","POST"])
def login():
  login_form=LoginForm()
  if login_form.validate_on_submit():
    user=User.query.filter_by(username=login_form.username.data).first()
    if user is not None and user.verify_password(login_form.password.data):
      login_user(user,login_form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))

    flash('Invalid username/password')
  title="Pomodoro Login"
  return render_template("auth/login.html",login_form=login_form,title=title)


@auth.route('/logout',methods=["GET","POST"])
@login_required
def logout():
  login_user()
  flash("Successfully logged out")
  return redirect(url_for("main.index"))