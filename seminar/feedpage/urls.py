from django.urls import path
from feedpage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/',views.new, name='new'),
    path('<int:id>/', views.show, name = 'show'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/update_home/', views.update_home, name='update_home'),
]