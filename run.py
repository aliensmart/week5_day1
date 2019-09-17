#! /usr/bin/env python3

from app import Account
from app import controller
from app import Position
from app import ORM
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'ttrader.db')
ORM.dbpath = DBPATH
# Account.dbpath = DBPATH
controller.run()

