from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import *

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('username','email','first_name','last_name','mobile')

    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ()
    fieldsets = ()
    class Meta:
        model = Account

admin.site.register(Account,AccountAdmin)