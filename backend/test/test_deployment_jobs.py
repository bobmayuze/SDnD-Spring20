import requests
import json

url = 'http://localhost:5000/jobs'
body = {
    "template_id" : "TEST",
    "region_id" : "sample_region_1",
    "target_queue" : "sample_region_1"
}

headers = {'content-type': 'application/json'}

for i in range(3):
    r = requests.put(url, data=json.dumps(body), headers=headers)

# url = 'http://localhost:5000/jobs'
# body = {
#     "task_id" : "75e4d96d-723a-49d9-8e98-570ccf0f68ff",
# }

# headers = {'content-type': 'application/json'}

# r = requests.delete(url, data=json.dumps(body), headers=headers)
