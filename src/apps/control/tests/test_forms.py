from django.test import TestCase

from should_dsl import should, should_not

from apps.control.forms import ExpenseForm
from apps.control.models import Expense


class ControlFormTestCase(TestCase):

    def setUp(self):
        self.form = ExpenseForm()

    def test_it_has_a_form(self):
        self.form.instance |should| be_instance_of(Expense)

    def test_it_can_save_an_expense(self):
         self.form = ExpenseForm({'value': 1, 'category': 'food', 'description': 'Rice', 'date': '01/01/2011'})
         self.form.save()
         self.form.data['value'] |should| equal_to(1)

    def test_it_cannot_save_an_expense_without_value(self):
        parameters = {'category': 'food', 'description': 'Rice', 'date': '01/01/2011'}
        self.form = ExpenseForm(parameters)
        self.form.is_valid() |should| be(False)
        self.form.save |should| throw(ValueError)

    def test_it_can_save_without_description(self):
        parameters = {'value': 100.0, 'category': 'gym', 'date': '20/06/2011'}
        self.form = ExpenseForm(parameters)
        self.form.is_valid() |should| be(True)
        self.form.save |should_not| throw(ValueError)
