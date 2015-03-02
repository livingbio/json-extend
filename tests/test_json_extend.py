from unittest2 import TestCase
from json_extend import *

from datetime import datetime, date

class TestStorage(TestCase):
    def test_all(self):
        self.assertEqual(loads(dumps({})), {})

        obj = {
            "date": date(2015, 1, 2),
            "datetime": datetime(2015, 1, 2, 3, 4, 5, 6)
        }
        self.assertEqual(loads(dumps(obj)), obj)
        # self.assertEqual(loads(dumps(_date)), _date)

