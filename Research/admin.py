from django.contrib import admin
#from .models import Author, Editor, Product, employee
#from Research.admin_site import custom_admin_site
from django.contrib.admin import SimpleListFilter
from django.urls import reverse
from django.utils.html import format_html
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportActionModelAdmin
'''
from tickets.forms import TicketAdminForm
'''
from .models import Venue, ConcertCategory, Concert, Ticket



'''class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)'''

#the register decorator
'''@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
# no need to pass admin.site.register(Author, AuthorAdmin)  again

#we can also pass other models in a single one using register decorator
@admin.register(Author, Editor, site=custom_admin_site)
class PersonAdmin(admin.ModelAdmin):
    pass

#ModelAdmin.actions

def mark_as_delivered(modeladmin , request , queryset):
    queryset.update(status='delivered')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','status')
    actions = [mark_as_delivered]
    actions_on_top = True 
    empty_value_display = "-empty-"
    date_hierarchy = "delivered_date" # Show actions at the top
    #actions_on_bottom = True  # Show actions at the bottom
    #actions_selection_counter = False  # Disable the selection counter
#when both are true  the action will be showed on both top and bottom
admin.site.register(Product , ProductAdmin)

#empty_value_display using register decorator
class employeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')

    @admin.display(empty_value="empty")
    def post(self, obj):
        return obj.post
    
admin.site.register(employee , employeeAdmin)
'''

class ConcertInline(admin.TabularInline):#manage related models directly in the admin interface of the parent model.
    model = Concert
    fields = ["name", "starts_at", "price", "tickets_left"]
    readonly_fields = ["name", "starts_at", "price", "tickets_left"]#Makes the specified fields read-only, so they can be viewed but not edited.
    max_num = 0#Prevents adding new Concert records directly from the inline interface.
    extra = 0
    can_delete = False#Disables the option to delete related Concert records from the inline.
    show_change_link = True#Adds a link to edit the specific Concert record from the inline view.


class VenueAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "capacity"]
    inlines = [ConcertInline]#Includes the ConcertInline in the Venue admin, allowing inline management of related Concert objects.


class ConcertCategoryAdmin(admin.ModelAdmin):
    pass


class SoldOutFilter(SimpleListFilter):
    title = "Sold out" # Defines the display name of the filter in the admin interface.
    parameter_name = "sold_out"

    def lookups(self, request, model_admin):
        return [
            ("yes", "Yes"),
            ("no", "No"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.filter(tickets_left=0)#If the value is "yes", it filters concerts with tickets_left=0.
        else:
            return queryset.exclude(tickets_left=0)


class ConcertAdmin(admin.ModelAdmin):
    list_display = ["name", "display_venue", "starts_at", "display_price", "tickets_left", "display_sold_out"]
    list_select_related = ["venue"]
    search_fields = ["name", "venue__name", "venue__address"]
    list_filter = ["venue", SoldOutFilter]
    readonly_fields = ["tickets_left"]

    def display_sold_out(self, obj):
        return obj.is_sold_out()

    display_sold_out.short_description = "Sold out"
    display_sold_out.boolean = True

    def display_price(self, obj):
        return f"${obj.price}"

    display_price.short_description = "Price" #Generates a clickable link to the admin edit page of the related Venue.
    display_price.admin_order_field = "price"

    def display_venue(self, obj):
        link = reverse("admin:tickets_venue_change", args=[obj.venue.id])
        return format_html('<a href="{}">{}</a>', link, obj.venue)

    display_venue.short_description = "Venue"


@admin.action(description="Activate selected tickets")
def activate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Deactivate selected tickets")
def deactivate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=False)


class TicketAdmin(DjangoQLSearchMixin,  ImportExportActionModelAdmin):
    list_display = ["customer_full_name", "concert", "payment_method", "paid_at", "is_active"]
    list_select_related = ["concert", "concert__venue"]
    actions = [activate_tickets, deactivate_tickets]
   # form = TicketAdminForm

admin.site.register(Venue, VenueAdmin)
admin.site.register(ConcertCategory, ConcertCategoryAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Ticket, TicketAdmin)
