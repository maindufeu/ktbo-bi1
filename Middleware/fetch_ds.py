import requests
import json
import subprocess

datastreams_id = [6,63,101,89,98,97,99]

for i in datastreams_id:
    url = f'https://KTBO.datatap.adverity.com/api/datastreams/{i}/fetch_fixed/'
    payload = json.dumps({
      "start": "2021-01-01T00:00:00Z",
      "end": "2021-05-10T00:00:00Z"
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Token c49e653ffa8a0c80768bbf1af0887905a56fff9b'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    print(response)
    print(":V")
