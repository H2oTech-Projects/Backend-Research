from django.contrib import admin
from .models import Author, Editor, Product
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

#ModelAdmin.actions

def mark_as_delivered(modeladmin , request , queryset):
    queryset.update(status='delivered')

class ProductAdmin(admin.ModelAdmin):
    actions = [mark_as_delivered]
    actions_on_top = True 
    date_hierarchy = "delivered_date" # Show actions at the top
    #actions_on_bottom = True  # Show actions at the bottom
    #actions_selection_counter = False  # Disable the selection counter
#when both are true  the action will be showed on both top and bottom
admin.site.register(Product , ProductAdmin)
