reductions = []
articles = []

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

#Data format [1,2,3,4,5...]
def setReductions(reducts):
    print(reducts)
    reductions = reducts
    print(reductions)

def getReductions():
    print(reductions)
    return reductions

def addArticle(price,qty):
    articles.append([].append(price,qty))

def getArticles():
    return articles

if __name__ == '__main__':
    helloWorld()
    print(calculate_sub_total(askUserToAddPriceAndQuantity()))
    print(helloWorld())
