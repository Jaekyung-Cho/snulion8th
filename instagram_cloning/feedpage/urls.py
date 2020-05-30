from django.urls import path
from feedpage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
]