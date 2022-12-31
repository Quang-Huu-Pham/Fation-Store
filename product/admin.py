from django.contrib import admin

from .models import Category, Product
# Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'image', 'name', 'slug',
                    'price', 'old_price', 'sale', 'created_at']

    list_filter = ['category', 'slug']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
