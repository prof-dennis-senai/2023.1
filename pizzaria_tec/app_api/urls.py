from django.urls import path

from . import views

urlpatterns = [
    path('carrinho/adicionar/<int:id>', views.adicionar),
]
