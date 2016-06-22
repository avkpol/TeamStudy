from django.contrib import admin
from .models import ManufactureProduct,\
    StoreProduct,\
    Manufacturer,\
    ProductCategory,\
    Agent,\
    Order,\
    Distributor



class ManufactureProductAdmin(admin.ModelAdmin):
    list_display = ('productName', 'manufPrice', 'manufDate', 'expDate')


class StoreProductAdmin(admin.ModelAdmin):
    list_display = ('prodTitle','productDesc', 'storePrice', 'slug',
                    'receiveDate', 'inStock', 'discount', 'category')

admin.site.register(ManufactureProduct, ManufactureProductAdmin )
admin.site.register(Manufacturer)

admin.site.register(Order)
admin.site.register(StoreProduct, StoreProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Agent)
admin.site.register(Distributor)