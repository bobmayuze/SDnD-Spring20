import requests
import json
import pprint

# url = 'http://localhost:5000/templates'
# headers = {'content-type': 'application/json'}
# params = {'key_word':'T'}
# result = requests.get(url, params)


url = 'http://localhost:5000/templates'
headers = {'content-type': 'application/x-www-form-urlencoded'}
file_path = 'requirements.txt'

template_info = {
    "files" : ('file_name.txt', open(file_path, 'rb')),
    "name" : "Template-A",
    "description" : "This is a demo template",
    "Tags" : "TypeA"
}

result = requests.put(url,files=template_info)

pprint.pprint(result.json())