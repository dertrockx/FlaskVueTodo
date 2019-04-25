from flask import Flask
from flask_cors import CORS


def create_app(app_name='SURVEY_API'):  
    app = Flask(app_name)
    app.config.from_object('application.config.BaseConfig')

    from application.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    from application.models import db
    db.init_app(app)

    CORS(app)

    return app