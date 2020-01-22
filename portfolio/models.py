from django.db import models

# Create your models here.


class Projects(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images')
    urlfield = models.URLField(max_length=200)
    summary = models.CharField(max_length=200)
    github = models.URLField(max_length=255)

    def __str__(self):
        return self.title[:25]

    def url(self):
        return self.urlfield
