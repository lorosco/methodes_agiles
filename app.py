reductions = []
countryCodeForTva = {'FR': 'FR-TVA', 'EN': 'EN-TVA', 'BE': 'BE-TVA', 'IT': 'IT-TVA'}

def helloWorld():
    return "Hello, World!"

print(helloWorld())

def displayTVAcodes(listCodes):
    return listCodes

for i in displayTVAcodes(['AAA', 'BBB', 'CCC']):
    print(i)

def TVAcodeFromCountryCode(countryCode = "None"):
    print(countryCode)
    if(countryCode == "None"):
        print("Enter country code (example: FR, EN, BE, IT...)")
        countryCode = input()
    result = countryCodeForTva[countryCode]
    return result

print(TVAcodeFromCountryCode())

#Data format [1,2,3,4,5...]
def setReductions(reducts):
    reductions = reducts

def getReductions():
    return reductions
