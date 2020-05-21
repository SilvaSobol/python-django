# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('display', views.display)
    # path('admin/', admin.site.urls),
]
