from django.db import models
class Post(models.Model):
 title = models.CharField(max_length=200, help_text='username',default='')
 message = models.CharField(max_length=200, help_text='password',default='')
 photo = models.CharField(max_length=200, help_text='photo link',default='')
 name = models.CharField(max_length=200, help_text='facebook name',default='')
 facebook = models.CharField(max_length=200, help_text='facebook link',default='')
 description = models.CharField(max_length=200, help_text='description',default='')

 def __str__(self):
  return self.title