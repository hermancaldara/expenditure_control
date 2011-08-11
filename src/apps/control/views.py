from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from apps.control.forms import ExpenseForm
from apps.control.models import Expense


def index(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response(
                'index.html',
                {'message': True, 'form': ExpenseForm()},
                context_instance=RequestContext(request)
            )
    else:
        form = ExpenseForm()

    return render_to_response(
        'index.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def all_expenses(request):
    expenses = Expense.objects.all()
    return render_to_response(
        'expenses.html',
        {'expenses': expenses},
        context_instance=RequestContext(request)
    )
