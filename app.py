reductions = [3,5,7,10,15]
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

def getReductions():
    return reductions

def addArticle(price,qty):

    articles.append([price,qty])

if __name__ == '__main__':
    helloWorld()
    print(calculate_sub_total(askUserToAddPriceAndQuantity()))
    print(helloWorld())
