from django.contrib import admin

from .models import Driver, Client, CltOrder

admin.site.register (Driver)
admin.site.register (CltOrder)
admin.site.register (Client)

