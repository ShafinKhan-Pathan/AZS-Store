from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AdminAccount(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active')
    list_display_links = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Account, AdminAccount)