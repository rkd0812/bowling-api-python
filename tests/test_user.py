import unittest

from tests.BaseCase import BaseCase


class TestGetUsers(BaseCase):

    def test_user_response(self):
        response = self.app.get('/users')
        print(response)
        self.assertEqual(response.status_code, 200)
