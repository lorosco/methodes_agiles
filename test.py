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

        self.assertEqual("Hello, World!", app.helloWorld())

    def test_displayTVAcodes(self):
        TVAcodes = ['AAA','BBB', 'CCC']
        self.assertEquals(['AAA', 'BBB', 'CCC'], app.displayTVAcodes(TVAcodes))

    #def test_11_isAllReductionsCorrectlySet(self):
    #    reductions = [3,5,7,10,15]
    #    app.setReductions(reductions)
    #    self.assertEqual(app.getReductions(),reductions)

    #def test_3_isAddArticlePossible(self):
    #    app.addArticle(13,10)
    #    app.addArticle(12,12)
    #    self.assertEqual(app.getArticles(),[[13,10],[12,12]])

unittest.main()
