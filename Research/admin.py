from django.contrib import admin
from .models import Author, Book, Publisher, Product, Order

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Product)
admin.site.register(Order)
