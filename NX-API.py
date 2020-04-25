# import requests
# import json

# target = "http://192.168.2.65/ins"
# switchuser = "admin"
# switchpassword = "admin"

# myheaders = {"content-type": "application/json"}
# payload = {
#     "ins_api": {
#         "version": "1.0",
#         "type": "cli_show",
#         "chunk": "0",
#         "sid": "1",
#         "input": "show ip int brief",
#         "output_format": "json",
#     }
# }
# response = requests.post(
#     target,
#     data=json.dumps(payload),
#     headers=myheaders,
#     auth=(switchuser, switchpassword),
#     verify=False,
# ).json()

# print(json.dumps(response, indent=2, sort_keys=True))



import requests
import json
switchuser = 'admin'
switchpassword = 'bAh7taPe'

target = 'https://192.168.2.67/ins'
myheader = {'content-type' : 'application/jason'}
payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show cdp nei",
    "output_format": "json"
  }
}

response = requests.post(target, data=json.dumps(payload), headers=myheader, auth=(switchuser, switchpassword), verify=False).json()

print(json.dumps(response, indent=2, sort_keys=True))