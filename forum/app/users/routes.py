from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.users.models import UserModel, UserFollow
from app.users.forms import UserRegistrationForm, UserLoginForm, EmptyForm
from app.extensions import db
from flask_login import login_user, logout_user, current_user


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


@blueprint.route("/user/<int:id>")
def user(id):
    following = False
    user = UserModel.query.get_or_404(id)
    form = EmptyForm()
    if current_user.is_authenticated:
        relation = UserFollow.query.filter_by(
            follower_id=current_user.id, followed_id=user.id
        ).first()

        if relation:
            following = True

    return render_template("users/user.html", user=user, form=form, following=following)


@blueprint.route("/follow/<int:user_id>", methods=["POST"])
def user_follow(user_id):
    form = EmptyForm()

    if form.validate_on_submit():
        user = UserModel.query.filter_by(id=user_id).first()

        if user is None:
            flash("User Not Found", "danger")
            return redirect(f"/user/{user_id}")

        if user == current_user:
            flash("You cannot follow yourself.", "warning")
            return redirect(f"/user/{user_id}")

        relation = UserFollow(follower_id=current_user.id, followed_id=user.id)
        db.sesstion.add(relation)
        db.session.commit()
        return redirect(f"/user/{user_id}")


@blueprint.route("/unfollow/<int:user_id>", methods=["POST"])
def user_unfollow(user_id):
    form = EmptyForm()

    if form.validate_on_submit():
        user = UserModel.query.filter_by(id=user_id).first()

        if user in None:
            flash("User Not Found", "danger")
            return redirect(f"/user/{user_id}")

        if user == current_user:
            flash("You cannot unfollow yourself.", "warning")
            return redirect(f"/user/{user_id}")

        relation = UserFollow.query.filter_by(
            follower_id=current_user.id, followed_id=user.id
        ).first()

        if not relation:
            flash("You are not following this user.", "warning")
            return redirect(f"/user/{user_id}")

        db.session.delete(relation)
        db.session.commit()
        return redirect(f"/user/{user_id}")

    return redirect(f"/user/{user_id}")
