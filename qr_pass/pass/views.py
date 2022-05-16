import datetime as dt
import webbrowser
from django.shortcuts import render, redirect, get_object_or_404

from .models import Customer
from .forms import PassForm


def create_key():
    return (str(dt.datetime.now())
            .replace(' ', '')
            .replace('-', '')
            .replace(':', '')
            .replace('.', '')
            )


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
    key = create_key()
    if form.is_valid():
        new_rec = form.save(commit=False)
        new_rec.key = key
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
    api_url = 'https://qrcode.tec-it.com/API/QRCode?data='
    my_url = 'http://127.0.0.1:8000/check/'
    url = api_url + my_url + key
    template = 'qr.html'
    context = {
        'url': url
    }
    # webbrowser.open(url, new=1, autoraise=True)
    # return redirect('passes:index')
    return render(request, template, context)


def check(request, key):
    template = 'access.html'
    user = get_object_or_404(Customer, key=key)
    context = {
        'access': user.access,
        'name': user.real_name
    }
    return render(request, template, context)
