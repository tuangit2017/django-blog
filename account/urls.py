
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    # login / logout urls
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #path('logout/', 'django.contrib.auth.views.logout', name='logout'),
    path('register/', views.register, name='register'),
    #path('team/',about_views.team_page),
    path('edit/', views.edit, name='edit'),
]
