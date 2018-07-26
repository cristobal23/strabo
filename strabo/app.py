#! ../env/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from strabo.controllers.main import main
from strabo.models import db
from strabo.extensions import cache
from strabo.settings import ProdConfig

__author__ = 'Cristóbal Villarroel'
__email__ = 'cristobal23@gmail.com'
__version__ = '0.1'


def create_app(object_name=ProdConfig):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. strabo.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize the cache
    cache.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    # register our blueprints
    app.register_blueprint(main)

    return app
