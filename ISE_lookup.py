#!/usr/bin/env python3
import requests
import urllib3
import xml.dom.minidom

'''This script is simple API caller for MAC lookup to ISE'''

#disabling SSL error
urllib3.disable_warnings()

url = 'https://szlnm189dha:9060/ers/config/endpoint/name/'
hdr = {
        'Accept': 'application/xml',
        'Authorization': 'Basic ZXJzYWRtaW46RW1ndXl0aDVhZw==',
        'Content-Type': 'application/xml'
        }

#MAC you wish to lookup
mac = input('Enter a MAC -> ')

res = requests.get(url + mac, headers = hdr, verify = False)
print(res.status_code)
output = xml.dom.minidom.parseString(res.text)
print(output.toprettyxml())



