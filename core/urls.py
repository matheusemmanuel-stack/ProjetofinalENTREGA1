from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cortes/', views.listar_cortes, name='cortes'),
    path('contato/', views.contato, name='contato'),
]