from django.shortcuts import render, redirect, get_object_or_404

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
        new_rec.save()
    return redirect('passes:index')


def edit(request, nick):
    user = get_object_or_404(Customer, username=nick)
    form = PassForm(
        request.POST or None,
        instance=user
    )
    if form.is_valid():
        form.save()
        return redirect('passes:index')
    template = 'index.html'
    var = Customer.objects.all()
    context = {
        'var': var,
        'form': form,
        'is_edit': True,
        'nick': nick
    }
    return render(request, template, context)


def delete(request, nick):
    user = get_object_or_404(Customer, username=nick)
    user.delete()
    return redirect('passes:index')


def get_qr(request, key):
    pass
