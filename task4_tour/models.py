from django.db import models
from django.utils.timezone import now



class Tourist(models.Model):

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='img/', blank=True, null=True )
    email = models.EmailField(null=True, blank=True)
    skype = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    choiceTour = models.ManyToManyField('Tour')

    def __unicode__(self):
        return unicode(self.last_name)

class Tour(models.Model):

    title = models.CharField(max_length=255)
    tourPrice = models.ForeignKey('PriceTourCategory')
    tourTransfer = models.ForeignKey('TransTourCategory')
    location = models.CharField(max_length=255)
    hotel =  models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    Date = models.DateField(default=now)
    inStock = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    tourOrdered = models.BooleanField(default=False)
    tourPayed = models.BooleanField(default=False)
    tourPartlyPayed = models.BooleanField(default=False)


    def __unicode__(self):
        return unicode(self.title)

class TransTourCategory(models.Model):

    transportation = models.CharField(max_length=255,blank=True, null=True )
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.transportation)


class TourDirectCategory(models.Model):

    country = models.CharField(max_length=255,blank=True, null=True )
    hotel = models.CharField(max_length=255,blank=True, null=True )
    price = models.ForeignKey('PriceTourCategory')

    def __unicode__(self):
        return unicode(self.country)


class PriceTourCategory(models.Model):

    season = models.CharField(max_length=255,blank=True, null=True )
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)


    def __unicode__(self):
        return unicode(self.season)


