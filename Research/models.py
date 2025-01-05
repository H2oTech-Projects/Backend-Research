from django.db import models

class Author(models.Model):
    name = models.CharField()
    number_of_book = models.IntegerField()
    latest_book = models.CharField()
    date_of_publication = models.DateField()

    def __str__(self):
        return self.name
    
class Author2(models.Model):
    name = models.CharField()
    number_of_book = models.IntegerField()
    latest_book = models.CharField()
    date_of_publication = models.DateField()

    def __str__(self):
        return self.name