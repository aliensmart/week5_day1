from app.orm import ORM
from app.util import get_price


class Position(ORM):
    
    tablename = "positions"
    fields = ['ticker', 'number_shares', 'account_pk']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.ticker = kwargs.get('ticker')
        self.number_shares = kwargs.get('number_shares')
        self.account_pk = kwargs.get('account_pk')

    def current_value(self):
        return round(self.number_shares * get_price(self.ticker), 2)
