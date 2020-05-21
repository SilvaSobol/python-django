# from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('', views.index)
    # path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()