from django.test import TestCase
from should_dsl import should


class ControlViewsTestCase(TestCase):

    def test_index(self):
        response = self.client.get('/')
        response.status_code |should| equal_to(200)
