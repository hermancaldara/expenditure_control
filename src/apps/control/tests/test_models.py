from django.test import TestCase

from should_dsl import should

from apps.control.models import Expense


class ControlTestCase(TestCase):

    def setUp(self):
        self.expense = Expense(value=20.0, category='food', date='01/01/2011')

    def test_it_has_value_and_category_and_date(self):
        self.expense.value |should| equal_to(20.0)
        self.expense.category |should| equal_to('food')
        self.expense.date |should| equal_to('01/01/2011')