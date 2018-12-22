from flask import Blueprint, redirect, render_template, session, request, flash, url_for
from app import *
from app.main.form import StackmailForm
from app.models import *
from app import login_required, login_user, current_user, logout_user

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
@main_blueprint.route("/welcome")
def welcome():
    return render_template("welcome.html")

@main_blueprint.route("/Home")
@login_required
def Home():
    questions = Questions.query.all()
    return render_template("home.html", questions=questions)