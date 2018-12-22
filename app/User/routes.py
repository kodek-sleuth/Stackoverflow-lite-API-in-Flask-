from flask import Blueprint, current_app
from app import *
from flask import redirect, render_template, session, request, flash, url_for
from app.User.form import SignUpForm, LoginForm, UpdateForm
from app.models import User, Users, Questions, Answers
from app import login_required, login_user, current_user, logout_user

User_blueprint = Blueprint('User', __name__)

@User_blueprint.route("/SignUp", methods=['GET','POST'])
def SignUp():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form = SignUpForm(request.form)
    if form.validate():
        hashed_pw=bcrypt.generate_password_hash(form.password.data)
        try:
            user=User(firstname=form.firstname.data, lastname=form.lastname.data, country=form.country.data, linkedIn=form.linkedIn.data, email=form.email.data, username=form.username.data, password=hashed_pw)
            user1=User.query.filter_by(username=form.username.data).first()
            user2=User.query.filter_by(email=form.email.data).first()
            
            if user1:
                flash("Username already taken","danger")

            elif user2:
                flash("Email already taken","danger")
            
            else:
                db.session.add(user)
                db.session.commit()
                flash("{} you have successfully Created Your account, Login Kindly".format(form.username.data), "success")
                return redirect(url_for("User.Login"))
        except:
            flash("Account  already has A user by that exact description","danger")
    
    return render_template("signup.html", form=form)

@User_blueprint.route("/Login", methods=['GET','POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('main.Home'))
    form = LoginForm(request.form)
    if form.validate():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("main.Home"))
            else:
                flash("Invalid Password or Username, Try Again","danger")
                return redirect(url_for("User.Login"))   
        except:
             flash("Invalid Credentials, Please either register or Retry with Correct Credentials","danger")
    return render_template("login.html", form=form)

@User_blueprint.route("/Profile")
@login_required
def Profile():
    image_file=url_for('static', filename='profile_picture/'+ current_user.image_file)
    current = current_user
    user = User.query.filter_by(id = current.id).first()
    return render_template("profile.html", user=user, image_file=image_file)

@User_blueprint.route("/updateprofile", methods=['GET', 'POST'])
@login_required
def updateprofile():
    usernow = current_user
    image_file = url_for('static', filename='profile_picture/'+current_user.image_file)
    form = UpdateForm(request.form)
    if form.validate():
        user_email = User.query.filter_by(email = usernow.email).first()
        user_username = User.query.filter_by(username = usernow.username).first()
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.country = form.country.data
        current_user.linkedIn = form.linkedIn.data
        db.session.commit()
        
        if form.email.data != current_user.email: 
            current_user.email = form.email.data
            db.session.commit()
            flash("Your Account has been Updated", 'success')
            return redirect(url_for('User.Profile'))
        
        elif form.username.data != current_user.username:
            current_user.username = form.username.data
            db.session.commit()
            flash("Your Account has been Updated", 'success')
            return redirect(url_for('User.Profile'))
                                    
        else:
            flash('Email or Password  already exist','warning')
            return redirect(url_for('User.Profile'))

    elif request.method=='GET':
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.country.data = current_user.country
        form.linkedIn.data = current_user.linkedIn
        form.email.data = current_user.email
        form.username.data = current_user.username
        
    return render_template("updateprofile.html", form=form, image_file=image_file)

@User_blueprint.route("/Seequestions")
@login_required
def Seequestions():
    image_file = url_for('static', filename='profile_picture/'+ current_user.image_file)
    return render_template("seequestions.html", image_file=image_file)
           
@User_blueprint.route("/deletequestion/<string:deletequestion_title>", methods=['GET','POST'])
@login_required
def deletequestion(deletequestion_title):
    image_file = url_for('static', filename='profile_picture/'+ current_user.image_file)
    current = current_user
    user = User.query.filter_by(id = current.id).first()
    questions = Questions.query.filter_by(Title = deletequestion_title).delete()
    db.session.commit()
    
    return render_template("profile.html", user=user, image_file=image_file)

@User_blueprint.route("/Logout")
@login_required
def Logout():
    logout_user()
    return redirect(url_for("main.welcome"))
