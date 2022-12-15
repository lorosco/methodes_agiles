from io import StringIO
import sys
import unittest
import app

class Tests(unittest.TestCase):
    def test_helloWorld(self):
        self.assertEqual("Hello, World!", app.helloWorld())

    def test_displayTVAcodes(self):
        TVAcodes = ['AAA','BBB', 'CCC']
        self.assertEquals(['AAA', 'BBB', 'CCC'], app.displayTVAcodes(TVAcodes))

    def test_11_isAllReductionsCorrectlySet(self):
        reductions = [3,5,7,10,15]
        app.setReductions(reductions)
        self.assertEqual(app.getReductions(),reductions)

unittest.main()
