from django.contrib import admin
from django.urls import path
from .views import home, about, moses
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('moses.html', views.moses, name="moses"),
  
]
