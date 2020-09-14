from django.contrib import admin
from BookingSystem.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['First_Name', 'Last_Name', 'Age', 'Mobile', 'Email', 'Address']
admin.site.register(Customer, CustomerAdmin)

