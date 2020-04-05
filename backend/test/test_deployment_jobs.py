import requests
import json

url = 'http://localhost:5000/jobs'
## IMPORTANT: change template_id to whatever _id is in the templates database
body = {
    "template_id" : "5e7fe684c3acf7834de776e3",
    "region_id" : "Beijing",
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
