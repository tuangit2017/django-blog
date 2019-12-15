
from django.urls import path, include

from . import views



urlpatterns = [
    
	path('', views.newblog, name='newblog'),

    #path('detail/<int:question_id>/', blog_views.detail, name='detail'),
    #path('detail/<int:post_id>/', blog_views.post_detail, name='detail'),
    #path('sec_detail/<int:post_id>/', blog_views.sec_post_detail, name='sec_detail'),
    #path('<str:slug>/', blog_views.blog_post_detail_view, name='third_detail'),


]
