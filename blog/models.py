from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
	STATUS_CHOICES = (
	   ('draft','Draft'),
	   ('published','Published'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User,default=1, on_delete=models.CASCADE, related_name='blog_posts')
	image   = models.ImageField(upload_to='images/', blank=True, null=True)
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return f"/blog/{self.slug}"


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)


#class Comment(models.Model):

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    comment_text = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    #def __init__(self, *args, **kwargs):
    #    super(Post, self).__init__(*args, **kwargs)


    def __str__(self):
        return self.comment_text
