from app import app, bcrypt, db
from flask import redirect, render_template, session, request, flash, url_for
from app.forms import SignUpForm, LoginForm, AskQuestion, AnswerForm, UpdateForm, StackmailForm
from app.models import User, Users, Questions, Answers
from app import login_required, login_user, current_user, logout_user

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/SignUp", methods=['GET','POST'])
def SignUp():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form = SignUpForm(request.form)
    if form.validate():
        hashed_pw=bcrypt.generate_password_hash(form.password.data)
        db.create_all()
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
                return redirect(url_for("Login"))
        except:
            flash("Account  already has A user by that exact description","danger")
    
    return render_template("signup.html", form=form)

@app.route("/Login", methods=['GET','POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form = LoginForm(request.form)
    if form.validate():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("Home"))
            else:
                flash("Invalid Password or Username, Try Again","danger")
                return redirect(url_for("Login"))   
        except:
             flash("Invalid Credentials, Please either register or Retry with Correct Credentials","danger")
    return render_template("login.html", form=form)

@app.route("/Users")
@login_required
def Users():
    user = User.query.all()
    return render_template("Users.html",user=user)

@app.route("/Seequestions")
@login_required
def Seequestions():
    image_file = url_for('static', filename='profile_picture/'+ current_user.image_file)
    return render_template("seequestions.html", image_file=image_file)
           
@app.route("/updateprofile", methods=['GET', 'POST'])
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
            return redirect(url_for('Profile'))
        
        elif form.username.data != current_user.username:
            current_user.username = form.username.data
            db.session.commit()
            flash("Your Account has been Updated", 'success')
            return redirect(url_for('Profile'))
                                    
        else:
            flash('Email or Password  already exist','warning')
            return redirect(url_for('Profile'))

    elif request.method=='GET':
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.country.data = current_user.country
        form.linkedIn.data = current_user.linkedIn
        form.email.data = current_user.email
        form.username.data = current_user.username
        
    return render_template("updateprofile.html", form=form, image_file=image_file)

@app.route("/Profile")
@login_required
def Profile():
    image_file=url_for('static', filename='profile_picture/'+ current_user.image_file)
    current = current_user
    user = User.query.filter_by(id = current.id).first()
    return render_template("profile.html", user=user, image_file=image_file)

@app.route("/deletequestion/<string:deletequestion_title>", methods=['GET','POST'])
@login_required
def deletequestion(deletequestion_title):
    image_file = url_for('static', filename='profile_picture/'+ current_user.image_file)
    current = current_user
    user = User.query.filter_by(id = current.id).first()
    questions = Questions.query.filter_by(Title = deletequestion_title).delete()
    db.session.commit()
    
    return render_template("profile.html", user=user, image_file=image_file)

@app.route("/Home")
@login_required
def Home():
    questions = Questions.query.all()
    return render_template("home.html", questions=questions)

@app.route("/askquestion", methods=['GET','POST'])
@login_required
def askquestion():
    form = AskQuestion(request.form)

    if form.validate():
        user=current_user
        question=Questions(Title=form.Title.data, Content=form.Body.data, User_id=user.id)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('Home'))

    return render_template("askquestion.html",form=form)

@app.route("/singlequestion/<int:singlequestion_id>", methods=['GET','POST'])
@login_required
def singlequestion(singlequestion_id):
    user =current_user
    form = AnswerForm(request.form)
    singlequestion = Questions.query.get_or_404(singlequestion_id)
    questions=Questions.query.filter_by(id = singlequestion_id).first() 
    user1 = User.query.filter_by(username=user.username).first()

    if form.validate(): 
        answer=Answers(Body=form.Body.data, Question_id=singlequestion_id)
        db.session.add(answer)
        db.session.commit()
     
        flash("You have successfully added an answer", "success")
        return redirect(url_for("Home"))
    
    return render_template("singlequestion.html", singlequestion=singlequestion, form=form, questions=questions, user1=user1)

@app.route("/Logout")
@login_required
def Logout():
    logout_user()
    return redirect(url_for("welcome"))
