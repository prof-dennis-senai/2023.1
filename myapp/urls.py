from django.urls import path
from myapp.views import home, sobre, contato

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
]
