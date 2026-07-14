from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_veiculos, name='lista_veiculos'),
    path('veiculo/<int:pk>/', views.detalhe_veiculo, name='detalhe_veiculo'),
]
