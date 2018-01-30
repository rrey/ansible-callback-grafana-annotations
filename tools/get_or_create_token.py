import httplib
import sys
import json
import argparse
from base64 import b64encode

URI = "/api/auth/keys"

parser = argparse.ArgumentParser()
parser.add_argument("--user", default="admin", help="login for basic authentication")
parser.add_argument("--passwd", default="admin", help="password for basic authentication")
parser.add_argument("--host", default="127.0.0.1", help="Grafana host address")
parser.add_argument("--port", default="3000", help="Grafana listen port")
args = parser.parse_args()

cred = "%s:%s" % (args.user, args.passwd)
HEADERS = {"Content-Type": "application/json", "Authorization": "Basic %s" % b64encode(cred).decode('ascii')}

http = httplib.HTTPConnection(args.host, args.port)
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
    http = httplib.HTTPConnection(args.host, args.port)
    http.request("DELETE", "%s/%d" % (URI, token_id), headers=HEADERS)
    response = http.getresponse()
    if response.status != 200:
        print "Failed to remove 'ansible-module' token [%s]" % response.read()
        sys.exit(1)

http = httplib.HTTPConnection(args.host, args.port)
http.request("POST", URI, '{"name": "ansible-module", "role": "Editor"}', headers=HEADERS)
response = http.getresponse()
if response.status != 200:
    print "Failed to create 'ansible-module' token"
    sys.exit(1)
print json.loads(response.read())["key"]
