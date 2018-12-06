from flask import Flask, redirect, request, render_template, session, logging, flash,url_for
from form import SignUpForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='2882822821728SAASAS8111'

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/SignUp", methods=['POST','GET'])
def SignUp():
    form = SignUpForm(request.form)

    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        country = form.country.data
        linkedIn = form.linkedIn.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        flash("You have successfully Created Your acount", "success")
        return redirect(url_for("Login"))
    
    return render_template("signup.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)



