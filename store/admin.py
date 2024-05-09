from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','slug', 'product_price','product_description', 'is_available', 'created_date','modified_date')
    list_display_links = ('product_name','slug', 'product_price')
    prepopulated_fields = {'slug' : ('product_name',)}


admin.site.register(Product, ProductAdmin)