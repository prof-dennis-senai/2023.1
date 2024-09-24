from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('finalizar/compra/', views.finalizar_compra, name='finalizar_compra'),
]
