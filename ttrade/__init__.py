from .account import Account
from .position import Position
from .trade import Trade
from .orm import ORM

def  setdb(dbpath):
    ORM.dbpath = dbpath