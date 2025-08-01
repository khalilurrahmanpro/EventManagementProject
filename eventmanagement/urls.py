from django.contrib import admin
from django.urls import path ,include 
from django.contrib.auth import views as auth_views
from django.urls import path
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('', views.event_list, name='event_list'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
]
