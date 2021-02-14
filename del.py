#!usr/bin/env python3

import requests
import urllib3
import xml.dom.minidom
import time
from datetime import datetime
import xmltodict
import sys
import argparse
import json

# disabling SSL error
urllib3.disable_warnings()

# URI to call API to
url = 'https://szlnm189dha:9060/ers/config/endpoint/name/'
url2 = 'https://szlnm189dha:9060/ers/config/endpoint/'
hdr = {
        'Accept': 'application/json',
        'Authorization': 'Basic ZXJzYWRtaW46RW1ndXl0aDVhZw==',
        'Content-Type': 'application/json'
        }

# Parsing setup
parser = argparse.ArgumentParser(description='MAC deletion tool')
parser.add_argument('MAC', type=str, help='put MAC you wish to delete')
arg = parser.parse_args()

def Deletion(MAC):
    res = requests.get(url + MAC, headers = hdr, verify = False)
    rem = json.loads(res.text)
    delmac = rem['ERSEndPoint']['id']
    Del = requests.delete(url2 + delmac, headers = hdr, verify = False)
    print("Respons code = ", Del.status_code)

    
if __name__ == "__main__":
    Deletion(arg.MAC)



