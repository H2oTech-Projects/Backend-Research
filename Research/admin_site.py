from django.contrib.admin import AdminSite

from .models import Author

class CustomAdminSite(AdminSite):
    site_header = "Custom Admin"
    site_title = "Custom Admin Portal"
    index_title = "Welcome to Custom Admin"

custom_admin_site = CustomAdminSite(name='custom_admin')

'''from django.contrib.admin import ModelAdmin
class AuthorAdmin(ModelAdmin):
    list_display = ('name', 'number_of_book')

custom_admin_site.register(Author, AuthorAdmin)
'''