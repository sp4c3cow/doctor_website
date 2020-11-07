from django.contrib import admin
from .models import Contact

class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'telegram', 'date']

admin.site.register(Contact, AdminContact)