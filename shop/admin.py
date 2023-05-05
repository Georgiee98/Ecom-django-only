from django.contrib import admin
from .models import Product, Order
# Register your models here.


admin.site.site_header = "E-commerce Site" # Django administration
admin.site.site_title = "E-COM SHOP" # Title
admin.site.index_title = "Manage E-COM Shop"   # Site Administration


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    list_display = ('title', 'price','category', 'discount_price', 'description')
    search_fields = ('title', 'price', 'category')
    change_category_to_default.short_description = "Default Category"
    actions = ('change_category_to_default',)
    fields = ('title', 'price',)
    list_editable = ('price', 'category',)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'adress', 'total')
    search_fields = ('name', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrdersAdmin)

