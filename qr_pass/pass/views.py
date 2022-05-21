import datetime as dt

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Customer, Logs
from .forms import PassForm
from .telegram import send_message


def create_key():
    return (str(dt.datetime.now())
            .replace(' ', '')
            .replace('-', '')
            .replace(':', '')
            .replace('.', '')
            )


@login_required
def index(request):
    template = 'index.html'
    var = Customer.objects.filter(master=request.user)
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
        new_rec.master = request.user
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
    var = Customer.objects.filter(master=request.user)
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
    return render(request, template, context)


def check(request, key):
    template = 'access.html'
    try:
        user = get_object_or_404(Customer, key=key)
    except Exception:
        send_message(
            f'Попытка использовать неверный код: {key} в: '
            f'{str(dt.datetime.now())[:-7]}'
        )
        return render(request, 'bad_qr.html')
    Logs.objects.create(user=user, success=user.access)
    message = (
            'Доступ запросил: ' +
            str(user.real_name) +
            '(' + str(user) + '), ' +
            'получил доступ: ' + str(user.access) +
            ', в: ' + str(dt.datetime.now())[:-7]
    )
    send_message(message)
    context = {
        'access': user.access,
        'name': user.real_name
    }
    return render(request, template, context)


@login_required
def logs(request):
    template = 'logs.html'
    log = Logs.objects.filter(user__master=request.user)
    context = {
        'log': log,
    }
    return render(request, template, context)
