from flask import Flask

from my_app.api.routes import api
from my_app.site.routes import site

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(site)

    return app