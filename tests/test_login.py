#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest

create_user = True


@pytest.mark.usefixtures("testapp")
class TestLogin:
    def test_login(self, testapp):
        """ Tests if the login form functions """

        rv = testapp.post(
            '/login',
            data=dict(email='firsty@emaily.com', password='supersafepassword'),
            follow_redirects=True,
        )

        assert rv.status_code == 200

    def test_login_fail(self, testapp):
        """ Tests if the login form fails correctly """

        rv = testapp.post(
            '/login',
            data=dict(email='firsty@emaily.com', password=''),
            follow_redirects=True,
        )

        assert rv.status_code == 200
