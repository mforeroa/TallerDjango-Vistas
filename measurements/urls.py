from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.measurements_view, name='measurements_view'),
    path('?id=<id>', views.measurements_view, name='measurements_view')
]