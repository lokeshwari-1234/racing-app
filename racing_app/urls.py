from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('teams/', views.team_list, name='team_list'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('teams/<int:pk>/delete/', views.team_delete, name='team_delete'),

    path('drivers/', views.driver_list, name='driver_list'),
    path('drivers/create/', views.driver_create, name='driver_create'),
    path('drivers/<int:pk>/edit/', views.driver_edit, name='driver_edit'),
    path('drivers/<int:pk>/delete/', views.driver_delete, name='driver_delete'),

    path('races/', views.race_list, name='race_list'),
    path('races/create/', views.race_create, name='race_create'),
    path('races/<int:pk>/edit/', views.race_edit, name='race_edit'),
    path('races/<int:pk>/delete/', views.race_delete, name='race_delete'),
]