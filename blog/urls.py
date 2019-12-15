
from django.urls import path, include
from django.contrib import admin
#from django.views.generic import TemplateView
#from coffeehouse.about import views as about_views
from . import views as blog_views

urlpatterns = [

    path('',blog_views.blog_index),
    path('<str:slug>/', blog_views.blog_post_detail_view, name='third_detail'),
    #path('',TemplateView.as_view(template_name='homepage.html')),
    #path('',blog_views.post_list),
    #path('detail/<int:question_id>/', blog_views.detail, name='detail'),
    #path('detail/<int:post_id>/', blog_views.post_detail, name='detail'),
    #path('sec_detail/<int:post_id>/', blog_views.sec_post_detail, name='sec_detail'),
]
