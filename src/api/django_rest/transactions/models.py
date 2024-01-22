from django.db import models
# from src.models.TransactionType import TransactionType


# Create your models here.

class Transaction(models.Model):
    account_id = models.CharField(max_length=100)
    # add choices=TransactionType.get_transaction_types()
    transaction_type = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.IntegerField()
    description = models.TextField()