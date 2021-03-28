from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Projects(models.Model):

    project_name = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=60,null=True)
    date = models.DateTimeField(auto_now_add=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='images/')
    like = models.ManyToManyField(User,related_name='like',blank=True)

    @property
    def Total_likes(self):
        return self.like.count()

    def __str__(self):
        return f'{self.project_name}' 

   

