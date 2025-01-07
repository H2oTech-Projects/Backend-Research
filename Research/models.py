from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)
    number_of_book =  models.IntegerField()
    latest_book = models.CharField(max_length=30)
    published_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')

    def __str__(self):
        return self.name
    
class Editor(models.Model):
    name = models.CharField(max_length=20)
    name_of_book =  models.CharField(max_length=20)
    

    def __str__(self):
        return self.name
