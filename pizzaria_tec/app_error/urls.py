from django.urls import path
from . import views

urlpatterns = [
    path('404/', views.erro_404, name='erro_404'),
]