reductions = []

from sympy import true


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
    reductions = reducts

def getReductions():
    return reductions

def calculate_total(lines):
    sum = 0
    for i in lines:
        sum += calculate_sub_total(i)
    return sum


helloWorld()
print(calculate_sub_total(askUserToAddPriceAndQuantity()))
print(helloWorld())
