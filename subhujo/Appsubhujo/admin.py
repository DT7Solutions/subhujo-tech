from django.contrib import admin
from .models import ContactData
# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Subject','Message')

admin.site.register(ContactData,AdminContact)