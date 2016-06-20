#! ../env/bin/python
# -*- coding: utf-8 -*-
from strabo.app import create_app


class TestConfig:
    def test_dev_config(self):
        """ Tests if the development config loads correctly """

        app = create_app('strabo.settings.DevConfig')

        assert app.config['DEBUG'] is True
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://localhost/strabo'
        assert app.config['CACHE_TYPE'] == 'null'

    def test_test_config(self):
        """ Tests if the test config loads correctly """

        app = create_app('strabo.settings.TestConfig')

        assert app.config['DEBUG'] is True
        assert app.config['SQLALCHEMY_ECHO'] is True
        assert app.config['CACHE_TYPE'] == 'null'
