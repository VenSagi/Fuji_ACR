import requests
import re
import json

def ocr_space_file(filename, overlay=False, api_key='K87220888588957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.json()

def parse_text(text):
    lines = text.split('\r\n')
    data = {}
    for line in lines:
        parts = line.split('.')
        if len(parts) >= 2:
            key = parts[0].strip()
            value = parts[-1].strip()
            data[key] = value
    return data


response = ocr_space_file('TimeSlip1.jpg')
text = response['ParsedResults'][0]['ParsedText']
data = parse_text(text)
print(json.dumps(data, indent=4))
