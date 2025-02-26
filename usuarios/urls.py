from django.urls import path
from .views import register_view, list_view, detail_view, delete_view, update_view, home_view

app_name = 'usuarios'

urlpatterns = [
    path('', home_view, name='home'),
    path('criar/', register_view, name='criar'),
    path('listar/', list_view, name='listar'),
    path('detalhe/<int:pk>/', detail_view, name='detalhe'),
    path('atualizar/<int:pk>/', update_view, name='atualizar'),
    path('deletar/<int:pk>/', delete_view, name='deletar'), 
]
