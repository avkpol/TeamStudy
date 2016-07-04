from django.db import models
from django.utils.timezone import now
from django.utils.encoding import smart_unicode
from django.db.models import Count

from .choises import CHILD_GENDER, SIZE_CHOICES

class Order(models.Model):

    title = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField(null=True, blank=True)
    payed = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    clt = models.ForeignKey("Client", verbose_name='Ordered by client')

    def order_sum(self):

        '''Returns the order total '''
        price = self.price
        quantity = self.quantity
        self.order_sum = price * quantity

        return self.order_sum


    def client_all_order_total(self):

        price = Order.objects.filter(clt=self.clt)
        quantity = Order.objects.filter(clt=self.clt)
        total = []
        for p,q in zip(price, quantity):
            total_order = p.price * q.quantity
            total.append(total_order)
            self.clt_total = sum(total)

        return self.clt_total


    def cashback(self):

        client = Order.objects.filter(clt=self.clt)
        total = self.order_sum
        if client:
            if len(client) <= 20:
                t = total * 3 / 100
            elif len(client) > 20:
                t = total * 4 / 100
            else:
                t = total * 5 / 100
            return t

    order_total = property(order_sum)
    client_total = property(client_all_order_total)
    cashback = property(cashback)

    def __unicode__(self):
        return unicode("ordered {} pizza/s {} on ${} total".format(self.quantity,
                                                        self.title,self.order_total))

class Client(models.Model):

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    child = models.ForeignKey('ClientChild')
    phone = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    reg_date = models.DateField(default=now)
    is_children = models.BooleanField(default=False)
    address = models.CharField(max_length=255)



    def __unicode__(self):
        return self.last_name

class ClientChild(models.Model):

    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender = models.CharField(max_length=255, choices=CHILD_GENDER)
    photo = models.ImageField(upload_to='img/', blank=True, null=True)



    def __unicode__(self):
        return unicode(self.name)



class Pizza(models.Model):

    pizza_title = models.CharField(max_length=50)
    pizza_size = models.CharField(max_length=50, choices=SIZE_CHOICES)

    def __str__(self):

        return unicode('%s%s' %(self.pizza_title , self.pizza_size ))

class OrderAddress(models.Model):

    address = models.CharField(max_length=500)

    class Meta:
        ordering = ['address']

    def __unicode__(self):

        return self.address


class Delivery(models.Model):

    order = models.ManyToManyField('Order')
    courier = models.ManyToManyField('Courier')
    payed = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    orderDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    client = models.ForeignKey('Client')

    def __unicode__(self):

        return self.client.address


class Courier(models.Model):

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='img/', blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    skype = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    fulf_order = models.ForeignKey('Order')

    def __unicode__(self):
        return smart_unicode(self.last_name)



