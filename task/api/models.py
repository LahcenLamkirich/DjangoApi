from statistics import mode
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    date_published = models.DateTimeField("Date published")
    def __str__(self):
        return '%s %s' % (self.title, self.completed)
