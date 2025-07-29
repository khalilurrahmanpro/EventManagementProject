from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('create/', views.create_event, name='event_create'),
    path('<int:pk>/update/', views.update_event, name='event_update'),
    path('<int:pk>/delete/', views.delete_event, name='event_delete'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.create_category, name='category_create'),
    path('categories/<int:pk>/update/', views.update_category, name='category_update'),
    path('categories/<int:pk>/delete/', views.delete_category, name='category_delete'),

    path('participants/', views.participant_list, name='participant_list'),
    path('participants/create/', views.create_participant, name='participant_create'),
    path('participants/<int:pk>/update/', views.update_participant, name='participant_update'),
    path('participants/<int:pk>/delete/', views.delete_participant, name='participant_delete'),

    path('dashboard/', views.dashboard, name='dashboard'),
]
