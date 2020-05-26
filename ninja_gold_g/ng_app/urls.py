
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('find', views.process),
    path('reset', views.reset)
]