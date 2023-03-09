from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.users.routes import blueprint as users_blueprint
from app.posts.routes import blueprint as posts_blueprint
import app.exceptions as error_exception


app = Flask(__name__)

# ** For Development insert 'config.DevelopmentConfig' and for Production insert 'config.ProductionConfig'.
app.config.from_object("config.DevelopmentConfig")


def register_blueprints(app):
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)


def register_error_handlers(app):
    app.register_error_handler(403, error_exception.forbidden_access)
    app.register_error_handler(404, error_exception.page_not_found)
    app.register_error_handler(410, error_exception.deleted_page)
    app.register_error_handler(500, error_exception.server_error)


db = SQLAlchemy(app)
register_blueprints(app)
register_error_handlers(app)


# ! Use app_context() to create the application before initializing the database.
app.app_context().push()


db.create_all()
