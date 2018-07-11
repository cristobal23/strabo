import pytest

from strabo.app import create_app
from strabo.models import db, User


@pytest.fixture()
def testapp(request):
    app = create_app('strabo.settings.TestConfig')
    client = app.test_client()

    db.app = app
    db.create_all()

    if getattr(request.module, "create_user", True):
        test_user = User('firsty', 'lasty', 'firsty@emaily.com', 'supersafepassword')
        db.session.add(test_user)
        db.session.commit()

    def teardown():
        db.session.remove()
        db.drop_all()

    request.addfinalizer(teardown)

    return client
