from django.forms import ModelForm
from apps.control.models import Expense


class ExpenseForm(ModelForm):

    class Meta:
        model = Expense
