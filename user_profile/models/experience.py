from django.db import models


class Experience(models.Model):
    username = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.designation} at {self.company}"
