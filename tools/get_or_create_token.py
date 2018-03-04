import httplib
import os
import sys
import json
import argparse
from base64 import b64encode

URI = "/api/auth/keys"
GRAFANA_USER = os.getenv("GRAFANA_USER", "admin")
GRAFANA_PASSWORD = os.getenv("GRAFANA_PASSWORD", "admin")
GRAFANA_HOST = os.getenv("GRAFANA_HOST", "127.0.0.1:3000")

cred = "%s:%s" % (GRAFANA_USER, GRAFANA_PASSWORD)
HEADERS = {"Content-Type": "application/json", "Authorization": "Basic %s" % b64encode(cred).decode('ascii')}

http = httplib.HTTPConnection(GRAFANA_HOST)
http.request("GET", URI, headers=HEADERS)
response = http.getresponse()
if response.status != 200:
    print response.read()
tokens = json.loads(response.read())

token_id = None
for token in tokens:
    if token.get("name") == "ansible-module":
        token_id = token.get('id')
if token_id:
    http = httplib.HTTPConnection(GRAFANA_HOST)
    http.request("DELETE", "%s/%d" % (URI, token_id), headers=HEADERS)
    response = http.getresponse()
    if response.status != 200:
        print "Failed to remove 'ansible-module' token [%s]" % response.read()
        sys.exit(1)

http = httplib.HTTPConnection(GRAFANA_HOST)
http.request("POST", URI, '{"name": "ansible-module", "role": "Editor"}', headers=HEADERS)
response = http.getresponse()
if response.status != 200:
    print "Failed to create 'ansible-module' token"
    sys.exit(1)
print json.loads(response.read())["key"]
