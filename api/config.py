import os
from dynaconf import FlaskDynaconf


CONFIGURATION_PATH = os.path.dirname(os.path.abspath(__file__))


def configure(app):
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    FlaskDynaconf(app, extensions_list="EXTENSIONS", root_path=CONFIGURATION_PATH)