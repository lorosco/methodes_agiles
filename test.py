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

    def test_displayTVAcodes(self):
        TVAcodes = ['AAA','BBB', 'CCC']
        self.assertEquals(['AAA', 'BBB', 'CCC'], app.displayTVAcodes(TVAcodes))

    def test_11_isAllReductionsCorrectlySet(self):
        reductions = [3,5,7,10,15]
        app.setReductions(reductions)
        self.assertEqual(app.getReductions(),reductions)
    
    def test_calculate_total(self):
        lines = [{"price": 10, "quantity": 2},{"price": 10, "quantity": 1},{"price": 5, "quantity": 2},{"price": 10, "quantity": 3}]
        self.assertEqual(app.calculate_total(lines),70)


unittest.main()
