from django.db import models
from authors.models import Author

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pages = models.IntegerField()
    editor = models.CharField(max_length=50)
    edition = models.IntegerField()
    publication_year = models.IntegerField()
    language = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20)
    cover = models.ImageField(upload_to='covers/%d/%m/%Y', blank=True)
    borrowed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
