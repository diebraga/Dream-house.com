from django.contrib import admin
from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    """ class for admin panel """
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'auctioneer')
    list_display_links = ('id', 'title')
    list_filter = ('auctioneer', )
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Property, PropertyAdmin)