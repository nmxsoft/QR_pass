from django.urls import path

from . import views


app_name = 'passes'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<str:nick>', views.edit, name='edit'),
    path('delete/<str:nick>', views.delete, name='delete'),
    path('get-qr/<str:key>', views.get_qr, name='get_qr'),
    path('check/<str:key>', views.check, name='check'),
    path('logs/', views.logs, name='logs'),
]
