from django.contrib import admin
from django.urls import path
from events import views


    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.event_list, name='event_list'),
    path('add/', views.event_create, name='event_create'),
    path('edit/<int:pk>/', views.event_update, name='event_update'),
    path('delete/<int:pk>/', views.event_delete, name='event_delete'),
]

