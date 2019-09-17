import os
import time
# from app.orm import ORM
from app import Account, Position, Trade, ORM

DIR = os.path.dirname(__file__)
DBFILENAME = 'ttrader.db'
DBPATH = os.path.join(DIR, DBFILENAME)


def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath
    
    mike_bloom = Account(username='mike_bloom', balance=10000.00)
    mike_bloom.set_password("password")
    mike_bloom.save()

    tsla_position = Position(ticker='tsla', number_shares=5, account_pk=mike_bloom.pk)
    tsla_position.save()

    fake_trade = Trade(ticker='tsla', quantity=2,type=1)
    fake_trade.save()
