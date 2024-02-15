from django.db import models
from django.contrib.auth.models import Permission, User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    address=models.TextField() 
    order_date=models.DateField(auto_now_add=True)
    order_amount=models.FloatField()
    def __str__(self):
        return self.order_amount
