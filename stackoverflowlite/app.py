from flask import Flask, redirect, request, render_template, session, logging, flash,url_for
from forms import SignUpForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='2882822821728SAASAS8111'

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
            flash("You are now in your Stack overflow account", "success")
            return redirect(url_for("welcome"))
        else:
            flash("You have unsuccessful data","danger")
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)



