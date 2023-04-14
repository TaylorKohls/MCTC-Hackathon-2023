from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv
import requests
import os

def apiCall():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


    response = requests.get(
        url='http://127.0.0.1:5000/customer',
        #headers=headers,
        timeout=60
    )

    return response.status_code

print(apiCall())