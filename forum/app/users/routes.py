from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.users.models import UserModel
from app.users.forms import UserRegistrationForm, UserLoginForm
from app.extensions import db
from flask_login import login_user, logout_user


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
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    return render_template("users/register.html", form=form)


@blueprint.route("/login", methods=["GET", "POST"])
def user_login():
    form = UserLoginForm()

    if form.validate_on_submit():
        user = UserModel.query.filter_by(username=form.username.data).first()
        login_user(user)
        flash("You logged in successfully.")
        return redirect("/")
    return render_template("users/login.html", form=form)


@blueprint.route("/logout")
def user_logout():
    logout_user()
    flash("You logged out successfully.")
    return redirect("/")


@blueprint.route("/profile")
def user_profile():
    return render_template("users/profile.html")
