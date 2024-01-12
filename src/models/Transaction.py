import datetime
from TransactionType import TransactionType

class Transaction:

    account_id: str = None
    transaction_type: TransactionType = None
    date: datetime = None
    amount: int = None
    description: str = None

    def __init__(self, account_id, date, amount, description):
        self.account_id = account_id
        self.date = date
        self.amount = amount
        self.description = description
        self.transaction_type = TransactionType.UNCLASSIFIED
    
    def classify_transaction(self, trx_type: TransactionType):
        self.transaction_type = trx_type
