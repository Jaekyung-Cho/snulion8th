from django.urls import path
from feedpage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:pk>/like_feed/', views.like_feed, name='like_feed'),
    path('<int:id>/new_comment', views.new_comment, name='new_comment'),
    path('logout_popup/', views.logout_popup, name='logout_popup'),
]