from flask import Flask

from app.users.routes import blueprint as users_blueprint
from app.posts.routes import blueprint as posts_blueprint
from app.extensions import db, migrate
import app.exceptions as error_exception


def register_blueprints(app):
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)


def register_error_handlers(app):
    app.register_error_handler(403, error_exception.forbidden_access)
    app.register_error_handler(404, error_exception.page_not_found)
    app.register_error_handler(410, error_exception.deleted_page)
    app.register_error_handler(500, error_exception.server_error)


app = Flask(__name__)

register_blueprints(app)
register_error_handlers(app)

# ** For Development insert 'config.DevelopmentConfig' and for Production insert 'config.ProductionConfig'.
app.config.from_object("config.DevelopmentConfig")

db.init_app(app)

# ! Use app_context() to create the application before initializing the database.
app.app_context().push()

# ! Import *UserModel* here to avoid "circular_imports".
from app.users.models import UserModel

migrate.init_app(app, db)
