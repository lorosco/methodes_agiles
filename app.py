
from sympy import true


def helloWorld():
    print("Hello, World!")

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



helloWorld()
print(calculate_sub_total(askUserToAddPriceAndQuantity()))
