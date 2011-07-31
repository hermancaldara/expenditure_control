from django.test import TestCase, Client

from should_dsl import should

from apps.control.views import index


class ControlViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        response.status_code |should| equal_to(200)
        response.context.has_key('form') |should| be(True)

    def test_submit_a_expense(self):
        response = self.client.post('/', 
            {'value': 10.0, 'category': 'food', 'description': 'Rice', 'date': '01/01/2011'}
        )
        response.status_code |should| equal_to(302)

    def test_submit_a_expense_with_error(self):
        response = self.client.post('/', 
            {'category': 'food', 'description': 'Rice', 'date': '01/01/2011'}
        )
        form = response.context.get('form')
        form.errors['value'] |should| equal_to([u'This field is required.'])
