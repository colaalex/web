from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-id')  # task required sorting by -added_at but in fact it works with id
    
    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):

    def __str__(self):
        return self.title
    
    def url(self):
        return reverse('question-details', args=[str(self.id)])

    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True, blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likes = models.ManyToManyField(User, related_name='question_like_user')


class Answer(models.Model):

    text = models.TextField()
    added_at = models.DateField(auto_now_add=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
