from django.db import models


class Social(models.Model):
    username = models.CharField(max_length=100)
    github = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username