from django.contrib import admin
from django.urls import path

from . import views #i.e. from the same directory (shown by a dot), import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about),
    path('', views.homepage),

]
