from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from apps.control.forms import ExpenseForm


def index(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ExpenseForm()

    return render_to_response(
        'index.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
