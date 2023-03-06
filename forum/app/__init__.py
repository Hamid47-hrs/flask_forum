from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.users.routes import blueprint as users_blueprint
from app.posts.routes import blueprint as posts_blueprint

app = Flask(__name__)

# ** For Development insert 'config.DevelopmentConfig' and for Production insert 'config.ProductionConfig'.
app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(users_blueprint)
app.register_blueprint(posts_blueprint)


db = SQLAlchemy(app)

# ! Use app_context() to create the application before initializing the database.
app.app_context().push()


db.create_all()
