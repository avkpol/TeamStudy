from django.db import models
from django.utils.timezone import now


class ManufactureProduct(models.Model):

    productName = models.CharField(max_length=255, verbose_name='Product', blank=True, null=True)
    manufPrice = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                            verbose_name='Manufacturer Price')
    manufDate = models.DateField(default=now, verbose_name='Manufacture Date')
    expDate = models.DateField(verbose_name='Expire Date', default=now)

    def __unicode__(self):
        return self.productName


class StoreProduct(models.Model):

    prodTitle = models.ForeignKey(ManufactureProduct)
    productDesc = models.TextField(max_length=3000, null=True, blank=True,
                                   verbose_name='Product Description')
    producer = models.ForeignKey('Manufacturer')
    image = models.ImageField(upload_to='img/', blank=True, null=True )
    storePrice = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True,
                                verbose_name='Store Price')
    slug = models.SlugField(blank=True, null=True)
    receiveDate = models.DateField(default=now, verbose_name='Receive Date')
    inStock = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    category = models.ForeignKey('ProductCategory')

    def __unicode__(self):
        return unicode(self.prodTitle)


class ProductCategory(models.Model):

    prodCat = models.CharField(max_length=50, verbose_name='Product Category')

    def __unicode__ (self):
        return self.prodCat


class Order(models.Model):

    prodOrdered = models.ForeignKey(StoreProduct)
    payed = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.prodOrdered)


class Manufacturer(models.Model):

    manufacturer = models.CharField(max_length=50, null=True, blank=True,
                                    verbose_name='Manufacturer')
    def __unicode__(self):
        return self.manufacturer


class Agent(models.Model):

    agent = models.CharField(max_length=50, null=True, blank=True,
                                    verbose_name='Trading intermediate')
    def __unicode__(self):
        return self.agent


class Distributor(models.Model):

    distTitle = models.CharField(max_length=50, blank=True, null=True, verbose_name='Distributor')

    def __unicode__(self):
        return self.distTitle