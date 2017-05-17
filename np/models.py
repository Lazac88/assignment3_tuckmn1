from django.db import models
from django.utils import timezone

CHOICES = (('National', 'National'), ('International', 'International'), ('Technology', 'Technology'), ('Sport', 'Sport'))

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    section = models.CharField(max_length=50, choices=CHOICES)
    textIntro = models.TextField()
    textFull = models.TextField()
    imageURL = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
