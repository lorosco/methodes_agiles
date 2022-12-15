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

    def test_1_helloWorld(self):
        self.assertEqual("Hello, World!", app.helloWorld())

    def test_6_displayTVAcodes(self):
        TVAcodes = ['AAA','BBB', 'CCC']
        self.assertEqual(['AAA', 'BBB', 'CCC'], app.displayTVAcodes(TVAcodes))

    def test_calculate_total(self):
        lines = [{"price": 10, "quantity": 2},{"price": 10, "quantity": 1},{"price": 5, "quantity": 2},{"price": 10, "quantity": 3}]
        self.assertEqual(app.calculate_total(lines),70)

    def test_11_isAllReductionsCorrectlySet(self):
        self.assertEqual(app.getReductions(),[3,5,7,10,15])

    def test_3_isAddArticlePossible(self):
        app.addArticle(13,10)
        app.addArticle(12,12)
        self.assertEqual(app.articles,[[13,10],[12,12]])
        
    def test_7_countryCodeForTVA(self):
        self.assertEqual(app.TVAcodeFromCountryCode("BE"),"BE-TVA")
        self.assertEqual(app.TVAcodeFromCountryCode("EN"),"EN-TVA")
        self.assertEqual(app.TVAcodeFromCountryCode("FR"),"FR-TVA")
        self.assertEqual(app.TVAcodeFromCountryCode("IT"),"IT-TVA")

unittest.main()
