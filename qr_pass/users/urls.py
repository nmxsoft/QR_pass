from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='logged_out.html'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='login.html'),
        name='login'
    ),
]
