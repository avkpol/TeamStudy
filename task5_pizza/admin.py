from django.contrib import admin
from .models import Pizza, Order, Courier, Client, ClientChild, Delivery



class OrderAdmin(admin.ModelAdmin):

    list_display = ('title','quantity', 'order_total', 'clt','order_date', 'client_total','cashback')

class ClientAdmin(admin.ModelAdmin):

    list_display = ('last_name','child')

class PizzaAdmin(admin.ModelAdmin):

    list_display = ('pizza_title','pizza_size')



admin.site.register(Order,OrderAdmin)
admin.site.register(Courier)
admin.site.register(Client, ClientAdmin)
admin.site.register(ClientChild)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Delivery)
