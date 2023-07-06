from django.contrib import admin
from product.models import *

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Basic Info",{"fields":[('name','slug','status')]}),
        ("Description",{"fields":[("description")]}),
    ]
    list_display = ['name','slug','created_by','created_at','status']
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name','slug','created_by']
    list_filter = ['name']

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Basic Info",{"fields":[('parent'),('name','slug','status')]}),
        ("Description",{"fields":[("description")]}),
    ]
    list_display = ['name','slug','created_by','created_at','status']
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name','slug','created_by']
    list_filter = ['name']

admin.site.register(Brand,BrandAdmin)
admin.site.register(Category,CategoryAdmin)