from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastroPublicacao, name='cadPost' ),
]