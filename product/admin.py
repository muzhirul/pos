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


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Basic Info",{"fields":[('name','slug','status'),('category'),('type')]}),
        ("Description",{"fields":[("description")]}),
    ]
    list_display = ['name','slug','created_by','created_at','status']
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name','slug','created_by']
    list_filter = ['name']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['brand','supplier','product','name','size','price','status']
    prepopulated_fields = {'slug':('name',)}
    list_filter = ['brand__name','supplier__name','status']
    search_fields = ['name','brand','supplier']

admin.site.register(Brand,BrandAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Item,ItemAdmin)