from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv
import requests
import os

# This function will find the customer by the customer ID
def find_customer():
    load_dotenv()
    basic_auth = HTTPBasicAuth(os.getenv('api_key'), os.getenv('secret'))

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


    response = requests.get(
        url=os.getenv('base_uat_url') + f"bank-node/customer-accounts/v1/customer/{os.getenv('customer_id')}",
        auth=basic_auth,
        headers=headers,
        timeout=60
    )

    if str(response.status_code) == '200':
        customer = response.json()
        name = f'{customer["customer"]["name"]["firstName"]} {customer["customer"]["name"]["lastName"]}'
        email = customer["customer"]["associatedEmail"]
        custID = customer["customer"]["customerID"]
        return name, email, custID, response.status_code

# This will retrieve the accounts for the customer
def get_accts():
    load_dotenv()
    basic_auth = HTTPBasicAuth(os.getenv('api_key'), os.getenv('secret'))

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


    response = requests.get(
        url=os.getenv('base_uat_url') + f"bank-node/customer-accounts/v1/customer/{os.getenv('customer_id')}/accounts",
        auth=basic_auth,
        headers=headers,
        timeout=60
    )
    
    resp = response.json()
    accts = []
    for acct in resp["accounts"]:
        accts.append(acct)
    checking = []
    savings = None
    cred_card = None
    for acct in accts:
        if 'checking' in acct["description"] and acct["accountType"] == 'DDA':
            checking.append(acct)
        elif acct["accountType"] == 'SAV':
            savings = acct
        elif acct["accountType"] == 'CCD':
            cred_card = acct
    return checking, savings, cred_card


def get_acct_details(acct_id):
    load_dotenv()
    basic_auth = HTTPBasicAuth(os.getenv('api_key'), os.getenv('secret'))

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


    response = requests.get(
        url=os.getenv('base_uat_url') + f"bank-node/customer-accounts/v1/account/{acct_id}",
        auth=basic_auth,
        headers=headers,
        timeout=60
    )

    account = response.json()["account"]
    cards = response.json()["cards"]

    return account, cards

def get_transactions(acct_id, tran_type):
    load_dotenv()
    basic_auth = HTTPBasicAuth(os.getenv('api_key'), os.getenv('secret'))

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


    response = requests.get(
        url=os.getenv('base_uat_url') + f"bank-node/customer-accounts/v1/account/{acct_id}/trans/{tran_type}",
        auth=basic_auth,
        headers=headers,
        timeout=60
    )

    transObj = response.json()

    trns = []
    for tran in transObj["transactions"]:
        trns.append(tran)
    return trns


def get_transaction_detail(trn_id):
    load_dotenv()
    basic_auth = HTTPBasicAuth(os.getenv('api_key'), os.getenv('secret'))

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


    response = requests.get(
        url=os.getenv('base_uat_url') + f"bank-node/customer-accounts/v1/transaction/{trn_id}",
        auth=basic_auth,
        headers=headers,
        timeout=60
    )

    trn = response.json()["transaction"]
    return trn

def get_merchant_codes():
    load_dotenv()
    basic_auth = HTTPBasicAuth(os.getenv('api_key'), os.getenv('secret'))

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


    response = requests.get(
        url=os.getenv('base_uat_url') + f"bank-node/reference/v1/codes/all",
        auth=basic_auth,
        headers=headers,
        timeout=60
    )

    
    codes = response.json()
    #for code in codes["codes"]:
    #    mccs.append(code)
    
    return codes

def get_purchase_category(mcc):
    load_dotenv()
    basic_auth = HTTPBasicAuth(os.getenv('api_key'), os.getenv('secret'))

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


    response = requests.get(
        url=os.getenv('base_uat_url') + f"bank-node/reference/v1/code/{mcc}",
        auth=basic_auth,
        headers=headers,
        timeout=60
    )

    return response.json()

def show_money_market_savings(monthlyInc, percSaved, openAmt):
    amt_to_save = monthlyInc * percSaved
    balance_two_years = openAmt + (amt_to_save * 24)
    balance_five_years = openAmt + (amt_to_save * 60)
    balance_ten_years = openAmt + (amt_to_save * 120)

    if balance_two_years >= 25000:
        balance_two_years = balance_two_years * 0.07
    
    if balance_five_years >= 25000:
        balance_five_years = balance_five_years * 0.175
    
    if balance_ten_years >= 25000:
        balance_ten_years = balance_ten_years * 3.5

    return balance_two_years, balance_five_years, balance_ten_years

if __name__ == "__main__":
    name, email, custID, status = find_customer()
    