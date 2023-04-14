from flask import Flask, jsonify, request
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)



@app.route("/customer", methods=["GET"])
def get_customer():
    customer = {
        'name': 'John Doe',
        'customerID': '6778681711',
        'email': 'johndoe@example.com'
    }

    return customer

@app.route("/accounts", methods=["GET"])
def get_accounts():
    accounts = {
        'checking': {
            'accountID': '114641456',
            'accountName': 'Checking'
        },
        'savings': {
            'accountID': '456754997',
            'accountName': 'Savings'
        },
        'creditCard': {
            'accountID': '8646449476',
            'accountName': 'Consumer Credit Card'
        }
    }

    return accounts

@app.route("/account-details", methods=["GET"])
def get_account_details():
    account_details = {
        'checking': {
            'accountID': '114641456',
            'accountName': 'Checking',
            'balance': 589.22,
            'creationDate': '10-22-21'
        },
        'savings': {
            'accountID': '456754997',
            'accountName': 'Savings',
            'balance': 500.00,
            'creationDate': '10-23-21'
        },
        'creditCard': {
            'accountID': '8646449476',
            'accountName': 'Consumer Credit Card',
            'balance': 780.00,
            'creationDate': '10-23-21'
        }
    }

    return account_details

@app.route("/transactions", methods=["GET"])
def get_transactions():
    transacts = {
        'checking': {
            't02685': {
                'merchant': 'Subway',
                'amount': 10,
                'date': '11-2-21'
            },
            't025747': {
                'merchant': 'Hot Topic',
                'amount': 35,
                'date': '11-7-21'
            },
            't028989': {
                'merchant': 'Staples',
                'amount': 60,
                'date': '11-15-21'
            },
            't0787925': {
                'merchant': 'Amazon',
                'amount': 95,
                'date': '11-28-21'
            },
        },
        'savings': {
            't15655': {
                'merchant': 'ATM Deposit',
                'amount': 100,
                'date': '11-2-21'
            },
            't158656': {
                'merchant': 'ATM Deposit',
                'amount': 350,
                'date': '11-7-21'
            },
            't139256': {
                'merchant': 'ATM Deposit',
                'amount': 600,
                'date': '11-15-21'
            },
            't1298589': {
                'merchant': 'ATM Deposit',
                'amount': 950,
                'date': '11-28-21'
            },
        },
        'creditCard': {
            't39596': {
                'merchant': 'Subway',
                'amount': 10,
                'date': '11-2-21'
            },
            't359589': {
                'merchant': 'Hot Topic',
                'amount': 35,
                'date': '11-7-21'
            },
            't356585': {
                'merchant': 'Staples',
                'amount': 60,
                'date': '11-15-21'
            },
            't365599': {
                'merchant': 'Amazon',
                'amount': 95,
                'date': '11-28-21'
            },
        }
    }

    return transacts

@app.route("/savings-simulator", methods=["GET"])
def show_money_market_savings():
    amt_to_save = 1800 * .25
    balance_two_years = 100 + (amt_to_save * 24)
    balance_five_years = 100 + (amt_to_save * 60)
    balance_ten_years = 100 + (amt_to_save * 120)

    if balance_two_years >= 25000:
        balance_two_years = balance_two_years * 0.07
    
    if balance_five_years >= 25000:
        balance_five_years = balance_five_years * 0.175
    
    if balance_ten_years >= 25000:
        balance_ten_years = balance_ten_years * 3.5

    return jsonify(balance_two_years, balance_five_years, balance_ten_years)



if __name__ == '__main__':
    app.run()