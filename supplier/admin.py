from django.contrib import admin
from supplier.models import *

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info',{'fields':[('name','slug','status'),('c_person','mobile')]}),
        ('Supplier Address',{'fields':[('address')]}),
    ]
    list_display = ['name','c_person','address','mobile','status']
    search_fields = ['name','c_person','address','mobile','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Supplier,SupplierAdmin)