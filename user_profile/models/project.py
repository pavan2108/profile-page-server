from django.db import models


class Project(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name
