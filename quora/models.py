from django.db import models


# Create your models here.

class Question(models.Model):
    _id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    graphs = models.BooleanField(default=False)
    Dp = models.BooleanField(default=False)
    trees = models.BooleanField(default=False)
    greedy = models.BooleanField(default=False)
    arrays = models.BooleanField(default=False)
    strings = models.BooleanField(default=False)


class Answer(models.Model):
    _id = models.AutoField(primary_key=True)
    answer = models.TextField()
    author = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # likes = models.IntegerField(default=0)
    # createdAt = models.DateTimeField()
