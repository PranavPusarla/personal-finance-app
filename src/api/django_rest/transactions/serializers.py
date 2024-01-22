from rest_framework import serializers
from transactions.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    model = Transaction
    fields = ['id', 'account_id', 'transaction_type', 'date', 'amount', 'description']