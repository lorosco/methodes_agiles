from io import StringIO
import sys
import unittest
import app

class Tests(unittest.TestCase):
    def test_helloWorld(self):
        self.assertEqual(True, True)
    
    def test_price_and_quantity(self):
        line = {"price": 10, "quantity": 2}
        self.assertEqual(app.calculate_sub_total(line), 20)


unittest.main()
