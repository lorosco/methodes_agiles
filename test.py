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

unittest.main()
