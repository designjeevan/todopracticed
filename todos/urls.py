from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<id>', views.details, name='details'),
 #   path('add/<id>', views.add, name='details'),
]