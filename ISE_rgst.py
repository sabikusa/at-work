#!usr/bin/env python3

import requests
import urllib3
import xml.dom.minidom
import time
from datetime import datetime
import xmltodict
from pprint import pprint
import sys

#disabling SSL error
urllib3.disable_warnings()

payload = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns4:endpointBulkRequest operationType="create"\
    resourceMediaType="vnd.com.cisco.ise.identity.endpoint.1.0+xml" xmlns:ns4="identity.ers.ise.cisco.com" xmlns:xsi=\
        "http://www.w3.org/2001/XMLSchema-instance"><ns4:resourcesList>'
payload2 = "</ns4:resourcesList></ns4:endpointBulkRequest>"

def main():
    args = sys.argv

    for ise in enumerate(args):
        ep = f"<ns4:endpoint><groupId>9d934d30-644c-11ea-a8ef-12e4691882e8</groupId><mac>{ise}</mac>\
            <staticGroupAssignment>true</staticGroupAssignment>\
            <staticProfileAssignment>false</staticProfileAssignment></ns4:endpoint>"
        payload += ep
        print('-' * 30)
        print('MAC{:02}'.format(str(ise))
    

    #URI to call API to
    url = "https://szlnm189ata:9060/ers/config/endpoint/bulk"

    headers = {
    'Accept': 'application/xml',
    'Authorization': 'Basic ZXJzYWRtaW46RW1ndXl0aDVhZw==',
    'Content-Type': 'application/xml'
    }

    payload += playload2
    
    # calling an API to ISE with the parameter
    response = requests.put(url, headers = headers, data = payload, verify = False)

    # getting a bulk status based on the response header from ISE
    inquiry = requests.get(response.headers['Location'], headers = headers, verify = False)

    print("response_status = ", response.status_code)

    doc = xmltodict.parse(inquiry.text)
    pprint(doc['ns2:bulkStatus']['ns2:resourceStatus']['@id'])

if __name__ == '__main__':
    main()







