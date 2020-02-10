from celery import Celery, Task 
from pymongo import MongoClient
import time

import config

app = Celery('tasks')
app.config_from_object(config)

@app.task()
def add(x, y):
    time.sleep(5)
    return x + y
    