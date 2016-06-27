from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^fechas/', views.fechas, name='fechas'),
    url(r'^home/', views.home, name='home'),
]
