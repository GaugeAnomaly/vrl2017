from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Petition(models.Model):
    title_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    votes = models.IntegerField(default=0)
    desc_text = models.CharField(max_length=1000)
    improvement = models.CharField(max_length=1000)
    picture = models.ImageField(default='hello/static/images/anatoomikum.jpg')

    def __str__(self):
        return self.title_text