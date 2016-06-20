#!/usr/bin/env python

import os

from flask_script import Manager, Shell, Server
from flask_script.commands import ShowUrls, Clean
from strabo.app import create_app
from strabo.models import db, User

# default to dev config
env = os.environ.get('STRABO_ENV', 'dev')
app = create_app('strabo.settings.%sConfig' % env.capitalize())

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)


def _make_context():
    """Return context dict for a shell session so you can access
       app, db, and the User model by default.
    """
    return {'app': app, 'db': db, 'User': User}


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """
    db.create_all()


manager.add_command("server", Server())
manager.add_command("urls", ShowUrls())
manager.add_command("clean", Clean())
# Creates a python REPL with several default imports in the context of the app
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == "__main__":
    manager.run()
