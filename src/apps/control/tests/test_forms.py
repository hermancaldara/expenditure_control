from django.test import TestCase

from should_dsl import should

from apps.control.forms import ExpenseForm
from apps.control.models import Expense


class ControlFormTestCase(TestCase):

    def test_it_has_a_form(self):
        form = ExpenseForm()
        form.instance |should| be_instance_of(Expense)
