from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    nacionality = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name
