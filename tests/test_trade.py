from unittest import TestCase
from app import ORM, Trade
import os

from data import schema, seed

DIR = os.path.dirname(__file__)
DBFILENAME = "_test.db"
DBPATH = os.path.join(DIR, DBFILENAME)

ORM.dbpath = DBPATH

class TestTrade(TestCase):

    def setUp(self):
        schema(DBPATH)
        seed(DBPATH)

    def tearDown(self):
        os.remove(DBPATH)

    def testOneTrade(self):
        trade = Trade(ticker="aapl", quantity=2, type=1)
        self.assertEqual(trade.ticker, "aapl")
        self.assertEqual(trade.quantity, 2)
        self.assertEqual(trade.type, 1)
        self.assertIsInstance(trade, Trade)

    def testSave(self):
        trade = Trade(ticker="EA", quatity=10, type=0)
        trade.save()
        self.assertEqual(trade.pk, 2)
        trade = Trade(pk = 2, ticker = "EA", quantity = 100, type = 1)
        self.assertEqual(trade.quantity, 100)

    def testDelete(self):
        trade = Trade(pk=2)
        trade.delete()

        self.assertEqual(trade.quantity, None)
        self.assertEqual(trade.type, None)
        self.assertEqual(trade.type, None)


    def testOneFromPk(self):
        trade = Trade().one_from_pk(pk=1)
        self.assertEqual(trade.ticker, 'tsla')
        self.assertEqual(trade.quantity, 2)
        self.assertEqual(trade.type, 1)

    def testAllFromWhereClause(self):
        trade = Trade().all_from_where_clause()
        self.assertEqual(trade[0].ticker, "tsla")
        self.assertEqual(trade[0].quantity, 2)
        self.assertEqual(trade[0].type, 1)