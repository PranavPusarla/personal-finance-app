import datetime
import TransactionType

class Transaction:

    account_id: str = None
    transaction_type: TransactionType = None
    date: datetime = None
    amount: int = None
    description: str = None
