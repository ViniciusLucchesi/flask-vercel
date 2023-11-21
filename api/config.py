import os
from dynaconf import FlaskDynaconf


CONFIGURATION_PATH = os.path.dirname(os.path.abspath(__file__))


def configure(app):
    FlaskDynaconf(app, extensions_list="EXTENSIONS", root_path=CONFIGURATION_PATH)