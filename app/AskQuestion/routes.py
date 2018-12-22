from app import *
from flask import Blueprint, redirect, render_template, session, request, flash, url_for
from app.AskQuestion.form import AskQuestionForm
from app.models import User, Users, Questions, Answers
from app import login_required, login_user, current_user, logout_user

AskQuestion_blueprint=Blueprint('AskQuestion', __name__)

@AskQuestion_blueprint.route("/AskQuestion", methods=['GET','POST'])
@login_required
def AskQuestion():
    form = AskQuestionForm(request.form)

    if form.validate():
        user=current_user
        question=Questions(Title=form.Title.data, Content=form.Body.data, User_id=user.id)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.Home'))

    return render_template("askquestion.html",form=form)