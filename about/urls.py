
from django.urls import path, include
#from django.contrib import admin
from django.views.generic import TemplateView
#from coffeehouse.about import views as about_views
from . import views as about_views

urlpatterns = [
    #path('',TemplateView.as_view(template_name='homepage.html')),
    path('',about_views.about_page),
    path('team/',about_views.team_page),
    path('projects',about_views.project_page),

]
