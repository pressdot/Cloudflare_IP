
import json
import urllib.request
resp = urllib.request.urlopen("https://ipinfo.io/AS13335/json?token=yourtoken")
f = open('all_ip.txt','w')
ele_json = json.loads(resp.read())
for ips in ele_json['prefixes']:
    f.write(ips['netblock']+"\n")
for ips in ele_json['prefixes6']:
    f.write(ips['netblock']+"\n")
f.close()