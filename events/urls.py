from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('categories/', views.category_list, name='category_list'),
    path('participants/', views.participant_list, name='participant_list'),
    path('events/create/', views.create_event, name='create_event'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('events/<int:pk>/edit/', views.update_event, name='update_event'),
]
