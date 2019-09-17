#! /usr/bin/env python3

from ttrade import Account
from ttrade import controller
from ttrade import Position
from ttrade import ORM
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'ttrader.db')
ORM.dbpath = DBPATH
# Account.dbpath = DBPATH
controller.run()

