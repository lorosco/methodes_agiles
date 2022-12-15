from io import StringIO
import sys
import unittest
import app
class Tests(unittest.TestCase):
    def test_1_helloWorld(self):
        self.assertEqual("Hello, World!", app.helloWorld())

    def test_6_displayTVAcodes(self):
        TVAcodes = ['AAA','BBB', 'CCC']
        self.assertEqual(['AAA', 'BBB', 'CCC'], app.displayTVAcodes(TVAcodes))

    def test_11_isAllReductionsCorrectlySet(self):
        reductions = [3,5,7,10,15]
        app.setReductions(reductions)
        self.assertEqual(app.getReductions(),reductions)
    
    def test_7_countryCodeForTVA(self):
        self.assertEqual(app.TVAcodeFromCountryCode("BE"),"BE-TVA")
        self.assertEqual(app.TVAcodeFromCountryCode("EN"),"EN-TVA")
        self.assertEqual(app.TVAcodeFromCountryCode("FR"),"FR-TVA")
        self.assertEqual(app.TVAcodeFromCountryCode("IT"),"IT-TVA")

unittest.main()
