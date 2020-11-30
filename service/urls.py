from . import views
from price import urls
from django.urls import path,include

urlpatterns = [
    path('', views.service, name='service'),
    path('<str:name>/price', include(urls) , name='price')
]