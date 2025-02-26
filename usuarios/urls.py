from django.urls import path
from .views import register_view, list_view

app_name = 'usuarios'

urlpatterns = [
    path('criar/', register_view, name='criar'),
    path('listar/', list_view, name='listar'),
]

