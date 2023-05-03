from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('fruits/', views.fruitsTable, name='fruits'),
    path('veg/', views.vegTable, name='vegetables'),
    path('medic/', views.medicTable, name='medicinal'),
    path('cereals/', views.cerealTable, name='cereals')
]