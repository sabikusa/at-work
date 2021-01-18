#!/usr/bin/env python3
import requests
import urllib3
import xml.dom.minidom
import argparse

'''This script is simple API caller for MAC lookup to ISE'''

#disabling SSL error
urllib3.disable_warnings()

parser = argparse.ArgumentParser(description='MAC registration checker')
parser.add_argument('MAC', type=str, help='put MAC you wish to check')
arg = parser.parse_args()

url = 'https://szlnm189dha:9060/ers/config/endpoint/name/'
hdr = {
        'Accept': 'application/xml',
        'Authorization': 'Basic ZXJzYWRtaW46RW1ndXl0aDVhZw==',
        'Content-Type': 'application/xml'
        }


def check(MAC):
        res = requests.get(url + MAC, headers = hdr, verify = False)
        print('resopnse code :', res.status_code)
        output = xml.dom.minidom.parseString(res.text)
        prett = output.toprettyxml()
        print(prett)

if __name__ == '__main__':
        check(arg.MAC)


