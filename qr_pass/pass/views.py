from django.shortcuts import render

from .models import Customer


def index(request):
    template = 'index.html'
    var = Customer.objects.all()
    context = {
        'var': var
    }
    return render(request, template, context)
