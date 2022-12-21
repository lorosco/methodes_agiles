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
        TVAcodes = {'AAA': 111,'BBB': 222, 'CCC': 333}
        self.assertEqual({'AAA': 111,'BBB': 222, 'CCC': 333}, app.displayTVAcodes(TVAcodes))

    def test_calculate_total(self):
        lines = [{"price": 10, "quantity": 2},{"price": 10, "quantity": 1},{"price": 5, "quantity": 2},{"price": 10, "quantity": 3}]
        self.assertEqual(app.calculate_total(lines),70)

    def test_11_isAllReductionsCorrectlySet(self):
        self.assertEqual(app.getReductions(),[3,5,7,10,15])

    # def test_3_isAddArticlePossible(self):
    #     app.addArticle(13,10)
    #     app.addArticle(12,12)
    #     self.assertEqual(app.articles,[{"price":13,"quantity":10},{"price":12,"quantity":12}])

    #def test_3_isAddArticlePossible(self):
    #    app.addArticle(13,10)
    #    app.addArticle(12,12)
    #    self.assertEqual(app.getArticles(),[[13,10],[12,12]])

    def test_5_1_newPriceItemFromTVA(self):
        totalHT = app.calculate_sub_total({'price': 10, 'quantity': 1})
        TVA = app.TVAcodeFromCountryCode("FR")
        priceTTC= totalHT + (totalHT*0.2)
        computedPrice = app.cartPriceWithTVA(totalHT,tva=TVA)
        self.assertEqual(priceTTC, computedPrice)

    def test_5_2_newPriceItemFromTVA(self):
        totalHT = app.calculate_sub_total({'price': 10, 'quantity': 1})
        countryCode = "FR"
        priceTTC= totalHT + (totalHT*0.2)
        computedPrice = app.cartPriceWithTVA(totalHT,countryCode=countryCode)
        self.assertEqual(priceTTC, computedPrice)
    
    def test_7_countryCodeForTVA(self):
        self.assertEqual(app.TVAcodeFromCountryCode("FR"), 20)
        self.assertEqual(app.TVAcodeFromCountryCode("GB"), 10)
        self.assertEqual(app.TVAcodeFromCountryCode("BE"), 12)
        self.assertEqual(app.TVAcodeFromCountryCode("CA"), 11)
        self.assertEqual(app.TVAcodeFromCountryCode("BA"), 0.5)

    def test_9_getReduction(self):
        totalHT = app.calculate_sub_total({'price': 10, 'quantity': 1})
        TVA = app.TVAcodeFromCountryCode("FR")
        priceTTC= totalHT + (totalHT*0.2)
        computedPrice = app.cartPriceWithTVA(totalHT,tva=TVA)
        self.assertEqual(0.0, app.getReduction(computedPrice))

    

unittest.main()
