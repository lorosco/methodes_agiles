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

    def test_3_isAddArticlePossible(self):
        app.addArticle(13,10)
        app.addArticle(12,12)
        self.assertEqual(app.articles,[{"price":13,"quantity":10},{"price":12,"quantity":12}])

    #def test_3_isAddArticlePossible(self):
    #    app.addArticle(13,10)
    #    app.addArticle(12,12)
    #    self.assertEqual(app.getArticles(),[[13,10],[12,12]])

    def test_5_1_newPriceItemFromTVA(self):
        article = {"articleName": "Poire à lavement", "quantity": 7, "price": 30, "countryCode": "GB"}
        TVA = app.TVAcodeFromCountryCode(article["countryCode"])
        priceFlat = 30*7
        priceWithTaxe = priceFlat + priceFlat*(float(10)/100)
        computedPrice = app.itemPriceWithTVA(article)
        self.assertEqual(priceWithTaxe, computedPrice)

    def test_5_2_newPriceCartWithTVA(self):
            articles = [
                {"articleName": "Poire à lavement", "quantity": 7, "price": 30, "countryCode": "GB"},
                {"articleName": "Item2", "quantity": 8, "price": 24.35, "countryCode": "FR"},
                {"articleName": "Item3", "quantity": 5, "price": 12.49, "countryCode": "BE"},
                {"articleName": "Item4", "quantity": 3, "price": 5, "countryCode": "BA"},
            ]
            total = app.cartPriceWithTVA(articles)
            #total = 0
            #for i in articles:
            #    itemPrice = i["price"]*i["quantity"]
            #    TVA = i["countryCode"]
            #    totalItemPrice = itemPrice + itemPrice*(float(TVA)/100)
            #    total += totalItemPrice
            computed = 7*30*1.1 + 8*24.35*1.2 + 5*12.49*1.12 + 3*5*1.005
            self.assertEqual(total, computed)
    
    def test_7_countryCodeForTVA(self):
        self.assertEqual(app.TVAcodeFromCountryCode("FR"), 20)
        self.assertEqual(app.TVAcodeFromCountryCode("GB"), 10)
        self.assertEqual(app.TVAcodeFromCountryCode("BE"), 12)
        self.assertEqual(app.TVAcodeFromCountryCode("CA"), 11)
        self.assertEqual(app.TVAcodeFromCountryCode("BA"), 0.5)

unittest.main()
