#!usr/bin/env python3

import requests
import urllib3
import xml.dom.minidom
import time
from datetime import datetime
import xmltodict
import sys

#disabling SSL error
urllib3.disable_warnings()

#URI to call API to
url = "https://szlnm189ata:9060/ers/config/endpoint/bulk"

headers = {
  'Accept': 'application/xml',
  'Authorization': 'Basic ZXJzYWRtaW46RW1ndXl0aDVhZw==',
  'Content-Type': 'application/xml'
}

def main():
    args = sys.argv
    payload = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns4:endpointBulkRequest operationType="create"\
    resourceMediaType="vnd.com.cisco.ise.identity.endpoint.1.0+xml" xmlns:ns4="identity.ers.ise.cisco.com" xmlns:xsi=\
        "http://www.w3.org/2001/XMLSchema-instance"><ns4:resourcesList>'
    payload2 = "</ns4:resourcesList></ns4:endpointBulkRequest>"
    for ise, arg in enumerate(args):
        ep = f"<ns4:endpoint><groupId>9d934d30-644c-11ea-a8ef-12e4691882e8</groupId><mac>{arg}</mac>\
            <staticGroupAssignment>true</staticGroupAssignment>\
            <staticProfileAssignment>false</staticProfileAssignment></ns4:endpoint>"
        payload += ep
        print('-' * 30)
        print('#{:02}'.format(ise))
        print('MAC:', arg)

    payload += payload2


    # calling an API to ISE with the parameter
    response = requests.put(url, headers = headers, data = payload, verify = False)

    # getting a bulk status based on the response header from ISE
    inquiry = requests.get(response.headers['Location'], headers = headers, verify = False)
    output = xml.dom.minidom.parseString(inquiry.text)
    prett = output.toprettyxml()

    print("-" * 30 + "\n" + str(datetime.now()) + "\nresponse_status = ", response.status_code, "\n")
    print(prett)

if __name__ == '__main__':
    main()







