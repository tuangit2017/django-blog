from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 
#from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager): 
    def get_queryset(self): 
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Article(models.Model): 
	STAT_CHOICES = ( 
		('draft', 'Draft'), 
		('published', 'Published'), 
	) 
	article_title = models.CharField(max_length=250) 
	slug = models.SlugField(max_length=250, unique_for_date='published_date')                           
	article_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_post')
	picture   = models.ImageField(upload_to='images/', blank=True, null=True)
	description = models.TextField() 
	published_date = models.DateTimeField(default=timezone.now) 
	created_date = models.DateTimeField(auto_now_add=True) 
	updated_date = models.DateTimeField(auto_now=True) 
	status_choice = models.CharField(max_length=10, choices=STAT_CHOICES, default='draft') 

	objects = models.Manager() # The default manager. 
	published = PublishedManager() # Our custom manager.
	#newTags = TaggableManager()

	class Meta: 
		ordering = ('-published_date',) 

	def __str__(self): 
		return self.article_title

	def get_absolute_url(self):
		return f"/newblog/{self.slug}"


class ArticleComment(models.Model): 
    article = models.ForeignKey(Article,
                             on_delete=models.CASCADE,
                             related_name='article_comments')
    name = models.CharField(max_length=80) 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 
 
    class Meta: 
        ordering = ('created',) 
 
    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.article)
