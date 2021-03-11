from flask_uploads import IMAGES, UploadSet,configure_uploads
from flask import Flask
from config import config_options
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint
    
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)

    # configure_uploads(app,photos)
    mail.init_app(app)
    app.secret_key = "123456"

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)


    # setting config
    from .request import configure_request
    configure_request(app)


    return app