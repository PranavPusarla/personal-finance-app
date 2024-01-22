from Transaction import Transaction

class Budget:

    total: int = None
    categories: dict = {} # string, int
    
    def addTransaction(self, trx: Transaction):
        trx_type = trx.transaction_type.name
        initialValue = self.categories[trx_type]
        newValue = initialValue + trx.amount
        self.categories[trx_type] = newValue
        self.total += trx.amount
    
    def getCategories(self):
        return self.categories

    def getTotal(self):
        return self.total
