from django.urls import path
from myapp.views import home, sobre, contato, usuarios

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
    path('usuarios/', usuarios),
    path('usuarios/<int:id>/', usuarios),
]
