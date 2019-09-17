from unittest import TestCase
from app import ORM, Position
import os

from data import schema, seed

DIR = os.path.dirname(__file__)
DBFILENAME = "_test.db"
DBPATH = os.path.join(DIR, DBFILENAME)

ORM.dbpath = DBPATH

class TestPosition(TestCase):

    def setUp(self):
        schema(DBPATH)
        seed(DBPATH)

    def tearDown(self):
        os.remove(DBPATH)
    
    def testOnePosition(self):
        position = Position(ticker = "aapl", number_shares = 3, account_pk=1)
        self.assertEqual(position.ticker, "aapl")
        self.assertEqual(position.number_shares, 3)
        self.assertEqual(position.account_pk, 1)
        self.assertIsInstance(position, Position)

    def testSave(self):
        position = Position(ticker = "aapl", number_shares = 3, account_pk=1)
        position.save()
        self.assertEqual(position.pk, 2)
    
    def testDelete(self):
        position = Position(pk=2)
        position.delete()
        self.assertEqual(position.ticker, None)

    def testOneFromWhereClause(self):
        position = Position().one_from_where_clause()
        self.assertEqual(position.ticker, "tsla")
        self.assertEqual(position.number_shares, 5)

    def testAllFromWhereClause(self):
        position = Position().all_from_where_clause()
        self.assertEqual(position[0].ticker, "tsla")
        self.assertEqual(position[0].number_shares, 5)


