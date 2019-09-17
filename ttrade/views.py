def welcome_menu():
    print("Welcome to terminal trader!")
    print("\t1-create account")
    print("\t2-login")
    print("\t3-Login with API key")
    print("\t4-quit")
    return input("your choice: ")


def main_menu():
    print()
    print("1. see balance & positions")
    print("2. deposit money")
    print("3. look up stock price")
    print("4. buy stock")
    print("5. sell stock")
    print("6. trade history")
    print("7. Get API")
    print("8. delete account")
    print("9. quit")

    return input("your choice: ")

def get_password():
    return input("your password: ")

def get_username():
    return input("your username: ")

def get_balance():
    return float(input("your balance: "))

def error():
    print("please check your username or password")

def bad_input():
    print("bad input!!")

def show_balance(balance):
    print("your balance is : ", balance)

def show_positions(positions):
    print("your positions")
    for position in positions:
        print("\tticker", position.ticker)
        print("\tnumber or share", position.number_shares)

def deposit_amount():
    return float(input("what's the amount you want to deposit? "))

def get_ticker():
    return input("ticker : ")

def stock_price(price):
    print("the price is : ", price)

def bad_stock(ticker):
    print("we are sorry this stock {} does not exist.".format(ticker))

def share_tobuy():
    return int(input("how many shares do you want to buy "))

def trades(trades):
    print("this is the trades")
    for trade in trades:
        print("\tticker {} amount {}".format(trade.ticker, trade.quantity))

def del_conf():
    print("are you sure you want to delete your account??")
    print("Enter Y(yes) and N(no)")
    return input("your choice: ")

def my_key(api_key):
    print("Your API key is {}".format(api_key))

def user_api():
    return input("what is your api? ")

