from django.urls import path

from . import views

urlpatterns = [
    path('carrinho/adicionar/<int:id>', views.adicionar),
    path('produto/', views.ProdutoView.as_view()),
    path('produto/<int:id>', views.ProdutoItenView.as_view()),
]
