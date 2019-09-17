from app.orm import ORM
import time


class Trade(ORM):

    tablename = "trades"
    fields = ['ticker', 'quantity', 'type', 'date', 'price', 'account_pk']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.ticker = kwargs.get('ticker')
        self.quantity = kwargs.get('quantity')
        self.account_pk = kwargs.get('account_pk')
        self.type = kwargs.get('type')
        self.date = kwargs.get('date', time.time())
        self.price = kwargs.get('price')
