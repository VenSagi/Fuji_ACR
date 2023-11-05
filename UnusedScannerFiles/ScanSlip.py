import json
import requests

with open("response2.json", "r") as f:
    data = json.load(f)

#print(data['receipts'][0].keys())

items = data['receipts'][0]['items']

for item in items:
    print(f"{item['description']} - {item['value']}")


'''url = 'https://ocr.asprise.com/api/v1/receipt'
imageFile = "TimeSlip4.jpg"


r = requests.post(url, data = { \
  'api_key': 'TEST',        # Use 'TEST' for testing purpose \
  'recognizer': 'auto',       # can be 'US', 'CA', 'JP', 'SG' or 'auto' \
  'ref_no': 'ocr_python_123', # optional caller provided ref code \
  }, \
  files = {"file": open(imageFile, "rb")})

with open("response2.json", "w") as f:
    json.dump(json.loads(r.text), f)

'''