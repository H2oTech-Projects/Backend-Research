from django.db import models
from .managers import AvailableManager

class IndiBookManager(models.Manager):#custom manager
    def get_queryset(self):
        return super().get_queryset().filter(author="Indi")
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    objects = models.Manager()# default manager
    indi_objects = IndiBookManager()


class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role="A")
    
class EditorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role="E")
    
class Person(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=1,choices={"A": ("Author"), "E": ("Editor")})

    people= models.Manager ()
    authors = AuthorManager()
    editors = EditorManager()



class Author(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    
    objects = AvailableManager() 

class Novel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 