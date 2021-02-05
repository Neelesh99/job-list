from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    name = models.CharField(max_length=200)
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()
    open = models.BooleanField(default=False)
    url = models.CharField(max_length=1000)
    cv_uploaded = models.BooleanField(default=False)
    cover_letter_uploaded = models.BooleanField(default=False)

    def __str__(self):
        return self.name
