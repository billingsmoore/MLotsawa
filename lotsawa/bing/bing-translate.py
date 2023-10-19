import requests, uuid, json

# Add your key and endpoint
key = "00a81aa9e90c4e6aa0c05f206d137634"
endpoint = "https://api.cognitive.microsofttranslator.com"


# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "eastus"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': 'bo',
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = []

with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/data/ankhi/bing-batches/test-batch.txt', 'r') as f:
    for line in f:
        body.append({'text': line})

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()
#print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/bing/response.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)