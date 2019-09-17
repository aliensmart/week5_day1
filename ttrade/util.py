import requests
from hashlib import sha256

USEFAKE = False
FAKESTOCK = 'STOCK'

def get_price(ticker):
    """ acquire current price of stock from the IEX Cloud API """
    if USEFAKE and ticker == FAKESTOCK:
        return 3.50
    endpoint = "https://cloud.iexapis.com/stable/stock/{}/quote?token=".format(ticker)
    token = "sk_6e5dcfbafe9848d8971f95f2a5b2e90a"
    response = requests.get(endpoint + token).json()
    return response['latestPrice']

def hash_password(password):
    """ converts a plain-text password to a sha256 hashed version, 
    for database storage and lookup """
    hasher = sha256()
    hasher.update(password.encode())
    return hasher.hexdigest()


# if __name__ == "__main__":
#     print(get_price('aapl'))
#     print(hash_password("Password"))
