from flask import Flask
from app.users.routes import blueprint as users_blueprint
from app.posts.routes import blueprint as posts_blueprint

app = Flask(__name__)

# ** For Development insert 'config.DevelopmentConfig' and for Production insert 'config.ProductionConfig'.
app.config.from_object('config.DevelopmentConfig')

app.register_blueprint(users_blueprint)
app.register_blueprint(posts_blueprint)
