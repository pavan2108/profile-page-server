from django.db import models


class Certification(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    issuing_authority = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} by {self.issuing_authority}"
