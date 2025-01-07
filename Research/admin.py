from django.contrib import admin
from .models import Author, Editor
from Research.admin_site import custom_admin_site

'''class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)'''

#the register decorator
'''@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass'''
# no need to pass admin.site.register(Author, AuthorAdmin)  again

#we can also pass other models in a single one using register decorator
@admin.register(Author, Editor, site=custom_admin_site)
class PersonAdmin(admin.ModelAdmin):
    pass