from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


#comment model
class Comment(models.Model):
	post = models.ForeignKey('blog.Post', on_delete=models.CASCADE,
		related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default= False)

	def approve (self):
		self.approveed_comment = True
		self.save()

	def __str__(self):
		return self.text

#event model
class Activities(models.Model):
    title 		= models.CharField(max_length=100)
    time  		= models.DateTimeField(blank = True)
    location    = models.CharField(max_length=200,default="This event hasn't set a location")
    content 	= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author 		= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
      return self.title

    def get_absolute_url(self):
       return reverse('act-detail', kwargs={'pk': self.pk})


