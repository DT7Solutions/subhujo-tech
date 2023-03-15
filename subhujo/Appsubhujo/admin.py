from django.contrib import admin
from .models import ContactData,AddJob
from Appsubhujo.views import linkedJobPosting
# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Subject','Message')

class AdminJob(admin.ModelAdmin):
    list_display=('Title','ShortDescription','LongDescription','JobRole','Location','Experince','Date')
    
    def save_model(self, request, obj, form, change):
        self.my_custom_method(obj)
        super().save_model(request, obj, form, change)
    
     # Define your custom method here
    def my_custom_method(self, obj):
        job_item = obj.__dict__
        linkedJobPosting(job_data=job_item)


admin.site.register(ContactData,AdminContact)
admin.site.register(AddJob,AdminJob)