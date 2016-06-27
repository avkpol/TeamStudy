from django.contrib import admin
from .models import Tour, Tourist, TourDirectCategory, PriceTourCategory, TransTourCategory

admin.site.register(Tour)
admin.site.register(Tourist)
admin.site.register(TourDirectCategory)
admin.site.register(PriceTourCategory)
admin.site.register(TransTourCategory)
