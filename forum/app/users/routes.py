from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.users.models import UserModel
from app.users.forms import UserRegistrationForm
from app.extensions import db


blueprint = Blueprint("users", __name__)


@blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = UserModel(
            username=form.username.data,
            email=form.email.data,
            age=form.age.data,
            password=form.password.data,
        )
        print(user)
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    return render_template("users/register.html", form=form)
