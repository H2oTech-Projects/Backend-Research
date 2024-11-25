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

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    established_year = models.IntegerField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.product)

