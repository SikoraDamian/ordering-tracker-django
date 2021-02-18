DAY-01 ( models planing )

class Order(models.Model):
    Request_number = models.ChardField(max_length = 12, null=False)
    Vendor = models.Choice
    Quote_number = models.ChardFiels(max_length = 25)
    Total = models.ChardField(max_length = 10)
    Delivery_date = mosels.DataField()
    Ereq_number = models.IntegerField
    Pr_Pcard_number =  models.ChardFields()
