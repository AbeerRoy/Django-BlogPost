from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    #By creating a foreignKey we can dynamically access the the post table 
    #By adding [on_delete = models.CASCADE] we essentially made sure all the value gets updated with each action  
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    #Returning to the post detail after creating a post using the primary key(pk)
    def get_absolute_url(self):
        return reverse('post-detail', kwargs= {'pk': self.pk})
    
    #def get_absolute_url(self):
    #    return reverse('user-posts', kwargs= {'username': self.username})
    
    
    # Creating dunder(double under score) str method [just for shell usage]

    # def __str__ (self,title):
    #     self.title = title
    
    # def __repr__(self):
    #     return 'Post: {}'.format(self.title)


# class Article(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True) #it will update only when object is created
  
  
# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     text = models.CharField(max_length=200)
#     created_on = models.DateTimeField(auto_now_add=True)