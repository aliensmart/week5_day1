#!/usr/bin/env python3
import json
from ttrade import views
from .account import Account
from .util import hash_password, get_price

def run():
    choice = views.welcome_menu()

    if choice == "1": #create account 
        name = views.get_username()
        password = views.get_password()
        hash_pass = hash_password(password)
        balance = views.get_balance()
        new_account = Account()
        new_account.username = name
        new_account.password_hash = hash_pass
        new_account.balance = balance
        new_account.api_key = new_account.generate_api_key()
        new_account.save()
        main_menu(new_account)

    elif choice == "2": #login
        username = views.get_username()
        password = views.get_password()
        account = Account.login(username, password)

        if not account:
            views.bad_input()
            
        else:
            main_menu(account)
            

    elif choice == "3": #login with api
        api = views.user_api()
        account = Account.api_authenticate(api)
        account.api_key = api
        account.save()
        
        if not account:
            views.error()
        else:
            main_menu(account)

    elif choice == "4":
        return


def main_menu(account):
    while True:
        choice = views.main_menu()

        if choice == "1": #see balance & positions
            balance = account.balance
            positions = account.get_positions()
            views.show_balance(balance)
            views.show_positions(positions)
            
        elif choice == "2": #deposite money
            amount = views.deposit_amount()
            account.deposit(amount)
            account.save()

        elif choice == "3": #look up stock price
            ticker = views.get_ticker()

            try:
                price = get_price(ticker)
                views.stock_price(price)

            except:
                views.bad_stock(ticker)

        elif choice == "4": #buy stock
            ticker = views.get_ticker()
            try:
                amount = views.share_tobuy()
                account.buy(ticker, amount)
                account.save()

            except: # TODO find error class
                views.bad_stock(ticker)


        elif choice == "5": #sell stock
            ticker = views.get_ticker()
            try:
                amount = views.share_tobuy()
                account.sell(ticker, amount)
                account.save()

            except:
                views.bad_stock

        elif choice == "6": #trade history
            trades = account.get_trades()
            views.trades(trades)

        elif choice == '7': # Get api
            api_key = account.get_api()
            views.my_key(api_key)
            account.save()

            
        elif choice == "8" :
            del_choice = views.del_conf()
            if del_choice == "Y":
                account.delete()
            elif del_choice=="N":
               main_menu(account) 
            else:
                views.bad_input()
            
        elif choice == "9":
            return
            
        else:
            views.bad_input()