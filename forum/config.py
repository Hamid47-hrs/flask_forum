from os import path
class Config:
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = '6280dbe0887c5b4ac64395970f9e87fcf364099158d7257439674302d4eb9f2a'
    SECRET_KEY = 'f6c350d9b3a7b310efd58fef60919604549e379a73083c571a5940bceb21586b'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ...

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(Config.BASE_DIRECTORY, 'app.db')