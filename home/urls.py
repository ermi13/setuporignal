from django.urls import path
from . import views
from service import urls

urlpatterns = [
    path('', views.home, name="home"),
    path('submit',views.feedback, name="submit")
]