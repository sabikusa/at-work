#!/usr/bin/env python3
import requests
import urllib3

'''This script is simple API caller for MAC registration to ISE'''

#disabling SSL error
urllib3.disable_warnings()

url = 'https://szlnm189dha:9060/ers/config/endpoint/bulk'
body1 = '''\
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ns4:endpointBulkRequest operationType="create" resourceMediaType="vnd.com.cisco.ise.identity.endpoint.1.0+xml" xmlns:ns4="identity.ers.ise.cisco.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <ns4:resourcesList>
'''

