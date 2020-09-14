import requests
import urllib3
import xml.dom.minidom
from datetime import datetime
import xmltodict
from pprint import pprint

#disabling SSL error
urllib3.disable_warnings()

#URI to call API to
url = "https://szlnm189ata:9060/ers/config/endpoint/bulk"

#this could be the list of MAC a requestor populated in the field. a wrong formatted mac is present in between.
mac = ['aa:bb:cc:dd:ee:ff', 'eekekdddls', 'aa:bb:cc:dd:ee:00', 'aa:bb:cc:dd:ee:01']

#type of endpoint a requestor selects in the field. each type has its own ID used in ISE service. value is what to be passed in the XML body.
eptype = {
'Printer(MFD)': '9d934d30-644c-11ea-a8ef-12e4691882e8',
'non-MLJ_PC': '9d934d30-644c-11ea-a8ef-12e4691882e8',
'Other(Data_vlan)': '9d934d30-644c-11ea-a8ef-12e4691882e8',
'IP_Phone': 'ce0c0340-644b-11ea-a8ef-12e4691882e8'
}

payload = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ns4:endpointBulkRequest operationType="create"\
    resourceMediaType="vnd.com.cisco.ise.identity.endpoint.1.0+xml" xmlns:ns4="identity.ers.ise.cisco.com" xmlns:xsi=\
        "http://www.w3.org/2001/XMLSchema-instance"><ns4:resourcesList>'

payload2 = "</ns4:resourcesList></ns4:endpointBulkRequest>"


for ise in mac:
    ep = f"<ns4:endpoint><groupId>9d934d30-644c-11ea-a8ef-12e4691882e8</groupId><mac>{ise}</mac>\
    <staticGroupAssignment>true</staticGroupAssignment>\
    <staticProfileAssignment>false</staticProfileAssignment></ns4:endpoint>"

    payload += ep

payload += payload2


headers = {
  'Accept': 'application/xml',
  'Authorization': 'Basic ZXJzYWRtaW46RW1ndXl0aDVhZw==',
  'Content-Type': 'application/xml'
}

# calling an API to ISE with the parameter
response = requests.put(url, headers = headers, data = payload, verify = False)

# getting a bulk status based on the response header from ISE
inquiry = requests.get(response.headers['Location'], headers = headers, verify = False)

print("response_status = ", response.status_code)

call_body = xml.dom.minidom.parseString(payload)
output = xml.dom.minidom.parseString(inquiry.text)

doc = xmltodict.parse(inquiry.text)

pprint(doc['ns2:bulkStatus']['ns2:resourceStatus']['@id'])

with open('Bulk_request.txt', 'w') as c:
  c.write(str(datetime.now()))
  c.write("\n\n")
  c.write(call_body.toprettyxml())
  
with open('Bulk_result.txt', 'w') as r:
  r.write(str(datetime.now()))
  r.write("\n")
  r.write("response_code = ")
  r.write(str(response.status_code))
  r.write("\n\n")
  r.write(output.toprettyxml())
