from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('concluir/<int:id>', views.concluir, name='concluir'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
]