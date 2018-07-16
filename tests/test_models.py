#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest

from strabo.models import db, User, Place

create_user = False


@pytest.mark.usefixtures("testapp")
class TestModels:
    def test_user_save(self, testapp):
        """ Test Saving the user model to the database """

        test_user = User('firsty', 'lasty', 'firsty@emaily.com', 'supersafepassword')
        db.session.add(test_user)
        db.session.commit()

        user = User.query.filter_by(email="firsty@emaily.com").first()
        assert user is not None

    def test_user_password(self, testapp):
        """ Test password hashing and checking """

        test_user = User('firsty', 'lasty', 'firsty@emaily.com', 'supersafepassword')

        assert test_user.email == 'firsty@emaily.com'
        assert test_user.check_password('supersafepassword')

    def test_place_walking_time(self, testapp):
        """ Test walking time calculation """

        test_place = Place()

        assert test_place.meters_to_walking_time(80) == 1

    def test_place_wiki_path(self, testapp):
        """ Test wiki url parsing """

        test_place = Place()

        assert (
            test_place.wiki_path('Buckingham Palace')
            == 'https://en.wikipedia.org/wiki/Buckingham_Palace'
        )
