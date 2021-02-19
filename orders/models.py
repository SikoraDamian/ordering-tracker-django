from django.db import models


VENDOR_CHOICES = [
    ('PHARMA', 'Pharma Stainless'),
    ('QED', 'QED'),
    ('DL', 'Dawnlough'),
    ('EMC', 'EMC'),
    ('McMasterCARR', 'McMasterCARR'),
]

ORDER_STATUS = [
    ('Quoted', 'Quoted'),
    ('Ordered', 'Ordered'),
    ('Delivered', 'Delivered'),
    ('Completed', 'Completed'),
]

QUOTE_STATUS = [
    ('Creating', 'Creating'),
    ('Sent_for_quotation', 'Sent_for_quotation'),
    ('Quoted', 'Quoted'),
    ('In_links', 'In_links'),
    ('Ordered', 'Ordered'),
    ('Delivered', 'Delivered'),
]

REQUEST_STATUS = [
    ('Quoted', 'Quoted'),
    ('Ordered', 'Ordered'),
    ('Completed', 'Completed'),
    ('On_hold', 'On_hold'),
]

class Request(models.Model):
    request_number = models.CharFields(max_length=20)
    descriptions = models.CharFields(max_length=120)
    request_status = models.CharFields(max_length=20, choices=REQUEST_STATUS)

class Quote(models.Model):
    quote_number = models.CharFields(max_length=20)
    total = models.CharFields(max_length=20)
    quote_status = models.CharFields(max_length=20, choices=QUOTE_STATUS)
    cad_shared = models.IntegerField(defoult=False)

class Order(models.Model):
    request_number_f = models.OneToOne(request_number, on_delete=models.CASCADE)
    quote_number_f = models.OneToOne(quote_number, on_delete=models.CASCADE)
    vendor = models.CharFields(max_length=20, choices=VENDOR_CHOICES)
    order_status =  models.CharFields(max_length=20, choices=ORDER_STATUS)
    ereq = models.CharFields(max_length=20)
    pr_pcard = models.CharFields(max_length=20)
    delivery = models.DateField()


