# This Script will generate the authentication token for Catalyst Center and then use that token to retrieve network device information from the Catalyst Center API. The retrieved data will be saved in a CSV file.

import csv  # Use when u working on CSV
import requests
import json   # Required when u converting the json data
import pandas as pd  # Use when u beautify the excel
from openpyxl import Workbook

# Catalyst Center details
CC_IP = "192.168.1.10"      # Replace with your Catalyst Center IP/FQDN
USERNAME = "DNACUser"       # Replace with your Catalyst Center Username
PASSWORD = "CatcPass"       # Replace with your Catalyst Center Password

url = f"https://192.168.1.10/dna/system/api/v1/auth/token"  # Example

url = f"https://{CC_IP}/dna/system/api/vl/auth/token"

Bresponse = requests.post(

url,

auth=(USERNAME, PASSWORD),

verify=False

# Disable certificate verification (lab only)

)

token = response.json() ["Token"]

print("Authentication Token:")

print (token)

url= f"https://{CC_IP}/dna/intent/api/vl/network-device"

headers = {

}

"X-Auth-Token": token,

"Content-Type": "application/json"

response = requests.get(

(

url,

headers=headers,

verify=False

print(response.status code)

print(response.json())
