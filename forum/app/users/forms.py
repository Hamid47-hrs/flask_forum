from re import search
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import ValidationError
from app.users.models import UserModel


class UserRegistrationForm(FlaskForm):
    username = StringField("Username : ")
    email = StringField("Email : ")
    age = IntegerField("Age : ")
    password = StringField("Password : ")
    confirm_pass = StringField("Confirm Password : ")

    def validate_username(self, username):
        user = UserModel.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username is already taken.")

        elif not search("[a-zA-Z]", username.data):
            raise ValidationError("Username should have at least one letter.")

    def validate_email(self, email):
        user = UserModel.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email already exists.")

        elif not search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email.data):
            raise ValidationError("The Email address is not valid.")

    def validate_age(self, age):
        if age.data < 18:
            raise ValidationError("You must be at least 18 years old.")

    def validate_password(self, password):
        special_chars = ["$", "!", "@", "#", "%", "&"]
        if len(password.data) < 8:
            raise ValidationError("Password length must be at least 8.")

        elif len(password.data) > 18:
            raise ValidationError("Password length must not be greater than 18.")

        elif not any(char.isdigit() for char in password.data):
            raise ValidationError("Password should have at least one number.")

        elif not any(char.isupper() for char in password.data):
            raise ValidationError("Password should have at least one uppercase letter.")

        elif not any(char.islower() for char in password.data):
            raise ValidationError("Password should have at least one lowercase letter.")

        elif not any(char in special_chars for char in password.data):
            raise ValidationError(
                "Password should have at least one special character."
            )

    def validate_confirm_pass(self, confirm_pass):
        if self.password.data != confirm_pass.data:
            raise ValidationError("Password should match its confirmation.")


class UserLoginForm(FlaskForm):
    username = StringField("Username : ")
    password = StringField("Password : ")

    def validate_username(self, username):
        user = UserModel.query.filter_by(username=username.data).first()

        if user:
            if user.password != self.password.data:
                raise ValidationError("The password in not correct.")
        else:
            raise ValidationError("There is no user with this username.")
