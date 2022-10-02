import requests
import json
a=requests.get("https://api.coincap.io/v2/assets").json()
with open("rohit.json","w") as s:
    json.dump(a,s,indent=4)
