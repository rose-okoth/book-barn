from flask import Blueprint
from flask import Flask

main = Blueprint('main',__name__)

from . import views

# def create_app(config_name):

#     app = Flask(__name__)

#     # Creating the app configurations
#     app.config.from_object(config_options[config_name])

#     # Initializing flask extensions
#     bootstrap.init_app(app)

#     # Registering the blueprint
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     # setting config
#     from .requests import configure_request
#     configure_request(app)


#     return app

