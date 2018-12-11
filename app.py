from flask import Flask,render_template,url_for,flash,redirect,request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import SignUpForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='2882822821728SAASAS8111'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app)

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/SignUp", methods=['GET','POST'])
def SignUp():
    form = SignUpForm(request.form)

    if form.validate():
        flash("You have successfully Created Your account", "success")
        return redirect(url_for("Login"))
    return render_template("signup.html", form=form)

@app.route("/Login", methods=['GET','POST'])
def Login():
    form = LoginForm(request.form)

    if form.validate():
        if form.username.data=='last_visual' and form.password.data=='BelieveinAllah':
            
            return redirect(url_for("Home"))
        else:
            flash("You have unsuccessful data","danger")
    return render_template("login.html", form=form)

@app.route("/Home")
def Home():
    return render_template("home.html")

@app.route("/Users")
def Users():
    return render_template("Users.html")

@app.route("/Profile")
def Profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)



