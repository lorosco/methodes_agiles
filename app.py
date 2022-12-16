reductions = []
articles = []
countryCodeForTva = {'FR': 20, 'GB': 10, 'BE': 12, 'CA': 11, 'BA': 0.5}

def helloWorld():
    return "Hello, World!"

def calculate_sub_total(line):
    return line['price'] * line ['quantity']

def askUserToAddPriceAndQuantity():
    price = 0
    while True:
        price = input('Enter price : ')
        if price.isnumeric:
            break
    quantity = 0
    while True:
        quantity = input('Enter quantity : ')
        if quantity.isnumeric:
            break
    return {'price': float(price), 'quantity': float(quantity)}

def displayTVAcodes(listCodes):
    return listCodes

for i in displayTVAcodes(['AAA', 'BBB', 'CCC']):
    print(i)

def TVAcodeFromCountryCode(countryCode = "None"):
    if(countryCode == "None"):
        countryCode = input("Enter country code (example: FR, EN, BE, IT...)")
    result = countryCodeForTva[countryCode]
    return result

def itemPriceWithTVA(article):
    TVA = TVAcodeFromCountryCode(article["countryCode"])
    priceFlat = calculate_sub_total(article)
    priceWithTaxe = priceFlat + priceFlat*(float(TVA)/100)
    return priceWithTaxe

def cartPriceWithTVA(articles):
    total = 0
    for i in articles:
        itemPrice = itemPriceWithTVA(i)
        # itemPrice = i["price"]*i["quantity"]
        # TVA = TVAcodeFromCountryCode(i["countryCode"])
        # totalItemPrice = itemPrice + itemPrice*(float(TVA)/100)
        total += itemPrice
    return total

#Data format [1,2,3,4,5...]
def setReductions(reducts):
    reductions = reducts

def getReductions():
    return reductions

def addArticle(price,qty):
    articles.append([].append(price,qty))

def getArticles():
    return articles

if __name__ == '__main__':
    helloWorld()
    print(calculate_sub_total(askUserToAddPriceAndQuantity()))
    print(helloWorld())
    print(TVAcodeFromCountryCode())

