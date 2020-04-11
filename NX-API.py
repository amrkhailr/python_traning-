import requests
import json

target = "http://192.168.2.65/ins"
switchuser = "admin"
switchpassword = "admin"

myheaders = {"content-type": "application/json"}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show ip int brief",
        "output_format": "json",
    }
}
response = requests.post(
    target,
    data=json.dumps(payload),
    headers=myheaders,
    auth=(switchuser, switchpassword),
    verify=False,
).json()

print(json.dumps(response, indent=2, sort_keys=True))