from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import TransactionQuerySet

class User(AbstractUser):
    pass

# created class called customer with account, name and balance
class Customer(models.Model):
    account = models.CharField(max_length=15, unique=True) 
    name = models.CharField(max_length=50, unique=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name
    

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('debit', 'Debit'),
        ('credit', 'Credit'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.CharField('Account', max_length=15, unique=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    date = models.DateField()

    objects = TransactionQuerySet.as_manager()

    def __str__(self):
        return f"{self.type} of {self.amount} on {self.date} by {self.user}" 

    class Meta:
        ordering = ['-date']   
