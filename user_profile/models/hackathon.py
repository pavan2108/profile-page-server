from django.db import models


class Hackathon(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    achievements = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.year})"
