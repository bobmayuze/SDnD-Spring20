from celery import Celery, Task 
from pymongo import MongoClient
import time

import config

app = Celery('task')
app.config_from_object(config)

@app.task()
def add(x, y):
    print(x)
    print(y)
    time.sleep(5)
    return str(x) + str(y)

    