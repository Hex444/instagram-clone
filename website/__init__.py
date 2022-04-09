# ever wanted to kill a person?
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'herctglshxifhoseriytihpcmoirpihighseo'

    from .views import views
    from .auth import auth
    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app