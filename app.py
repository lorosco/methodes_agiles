## Models

## Data

reductions = [3,5,7,10,15]
priceHT = 0
article = []
COUNTRY_CODE_FOR_TVA = {'FR': 20, 'GB': 10, 'BE': 12, 'CA': 11, 'BA': 0.5}
currentTVA = 0
currentReduc = 0

## Functions

def helloWorld():
    return "Hello, World!"

def calculate_sub_total(line):
    global priceHT
    priceHT = line ['price'] * line ['quantity']
    return priceHT

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

def displayTVAcodes(countryCodeForTva):
    for key,value in countryCodeForTva.items():
        print(key, ' ', value, "%")
    return countryCodeForTva

def TVAcodeFromCountryCode(countryCode = "None"):
    global currentTVA
    if(countryCode == "None"):
        countryCode = input("Enter country code: ")
    result = COUNTRY_CODE_FOR_TVA[countryCode]
    currentTVA += result
    return result

def itemPriceWithTVA(article):
    TVA = TVAcodeFromCountryCode(article["countryCode"])
    priceFlat = calculate_sub_total(article)
    priceWithTaxe = priceFlat + priceFlat*(float(TVA)/100)
    return priceWithTaxe

def cartPriceWithTVA(price, countryCode = "None", tva="None"):
    total = 0
    
    if(tva!="None"):
        total = price + (price*(tva/100))
    if(countryCode != "None"):
        tva = TVAcodeFromCountryCode(countryCode)
        total = price + (price*(tva/100))
    
    return total

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



# def addArticle(price,qty):
    # articles.append({"price":price,"quantity":qty})

## Main

if __name__ == '__main__':
    
    print(helloWorld())
    print("There you can find available country codes for VAT:")
    displayTVAcodes(COUNTRY_CODE_FOR_TVA)
    
    print(calculate_sub_total(askUserToAddPriceAndQuantity())," without taxes")
    print("TVA: ",TVAcodeFromCountryCode(),"%")
    print(cartPriceWithTVA(priceHT,tva=currentTVA), "TTC")
    # print("reduction: ",getReduction(cartPriceWithTVA(priceHT,currentTVA)))
    

