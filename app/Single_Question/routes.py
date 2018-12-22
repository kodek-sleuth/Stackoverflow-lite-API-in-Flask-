from flask import Blueprint, redirect, render_template, session, request, flash, url_for
from app import *
from app.Single_Question.form import AnswerForm
from app.models import User, Users, Questions, Answers
from app import login_required, login_user, current_user, logout_user

Single_Question_blueprint = Blueprint('Single_Question', __name__)

@Single_Question_blueprint.route("/singlequestion/<int:singlequestion_id>", methods=['GET','POST'])
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
        return redirect(url_for("main.Home"))
    
    return render_template("singlequestion.html", singlequestion=singlequestion, form=form, questions=questions, user1=user1)
