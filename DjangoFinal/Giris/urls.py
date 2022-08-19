from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from .views import GeziList
from .views import GeziView


urlpatterns = [
    #path('', views.ilksayfa, name='ilksayfa'),
    #path('menu2', views.ikincisayfa, name='ikincisayfa'),
    path('menu3', views.bilgi, name='bilgi'),
    path('', views.gezi_se, name='gezi-request'),
    path('menu2', GeziList.as_view(), name='gezi-list'),
    path('menu2/<int:pk>', GeziView.as_view(),name='gezi-ayrinti'),

    #path('bilgi', views.bilgi, name='bilgi'),


]
