from django.db import models
from django.utils.timezone import now
from django.utils import timezone
from django.utils.encoding import smart_unicode

MESAGE_TEXT = '''
              Last time you used our servise was 30 days ago.
              You are welcome to order our taxi again and have discount 20%
              '''


class Driver(models.Model):

    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='img/', blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    skype = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    fulf_order = models.ManyToManyField('CltOrder')
    auto = models.ManyToManyField('Auto')

    def __unicode__(self):
        return smart_unicode(self.last_name)


class CltOrder(models.Model):

    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    discont_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    distance = models.PositiveIntegerField()
    payed = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    orderDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    client = models.ForeignKey('Client')
    destination = models.CharField(max_length=100)

    def all(self):

        return self.filter(payed=True)

    def after30(self):

        order_date = CltOrder.objects.filter().order_by(self.orderDate)
        time_now = timezone.now()
        after30 = order_date + timezone.timedelta(days=30)
        if time_now == after30:
            return True

    def message(self):

        if self.after30 is True:
            return 'Dear %s,' + MESAGE_TEXT %(self.name)

    def client_name(self):

        return self.name

    def __unicode__(self):

        return '%s%s' %(self.client, self.destination)


class Client(models.Model):

    name = models.CharField(max_length=255)
    phone = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    date = models.DateField(default=now)

    def order_count(self, order=1):

        orders = CltOrder.objects.all()
        for self.order in orders:
            self.order += order
        return self.order

    def every_5(self):

        if self.order_count == 5:
            return True

    def has_discount(self):
        dcnt = CltOrder.discount
        if self.every_5 is True:
             dcnt.update(default=True)

    def __unicode__(self):

        return smart_unicode(self.name)

class Auto(models.Model):

    mark = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __unicode__(self):

        return self.number

