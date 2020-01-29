from django.contrib import admin

from .models import Contact, Contact_us

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'product_title', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'product_title')
  list_per_page = 25

class Contact_usAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)
admin.site.register(Contact_us, Contact_usAdmin)
