from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateField()

    def __str__(self):
        return self.title