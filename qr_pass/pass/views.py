from django.shortcuts import render, redirect

from .models import Customer
from .forms import PassForm


def index(request):
    template = 'index.html'
    var = Customer.objects.all()
    form = PassForm()
    context = {
        'var': var,
        'form': form
    }
    return render(request, template, context)


def create(request):
    form = PassForm(request.POST or None)
    if form.is_valid():
        new_rec = form.save(commit=False)
        # new_rec.username = request.username
        # new_rec.real_name = request.real_name
        new_rec.save()
    return redirect('passes:index')
