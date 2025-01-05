from django.contrib import admin
from .models import Author , Author2
'''
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
'''
admin.site.register(Author)
admin.site.register(Author2)

