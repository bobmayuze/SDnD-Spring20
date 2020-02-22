import requests
import json

url = 'http://localhost:5000/jobs'
body = {
    "template_id" : "SOME_TEMPLATE",
    "region_id" : "sample_region_1",
    "target_queue" : "sample_region_1"
}

headers = {'content-type': 'application/json'}

for i in range(10):
    r = requests.put(url, data=json.dumps(body), headers=headers)

# url = 'http://localhost:5000/jobs'
# body = {
#     "task_id" : "fd18e633-6fc7-4bd1-8b11-8c3799db2c20",
# }

# headers = {'content-type': 'application/json'}

# r = requests.delete(url, data=json.dumps(body), headers=headers)
