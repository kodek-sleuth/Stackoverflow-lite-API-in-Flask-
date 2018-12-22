from flask import Blueprint, current_app
from app import *
from flask import redirect, render_template, session, request, flash, url_for
from app.models import User, Users, Questions, Answers
from app import login_required, login_user, current_user, logout_user

Users_blueprint = Blueprint('Users', __name__)
@Users_blueprint.route("/Users")
@login_required
def Users():
    image_file = url_for('static', filename='profile_picture/'+current_user.image_file)
    user = User.query.all()
    return render_template("Users.html",user=user, image_file=image_file)
