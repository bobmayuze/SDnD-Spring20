# Celery task usage

## Start a worker
```sh
$ celery -A task worker -l INFO -n s1 -Q sample_region_1
```

## Start a monitor
```sh
$ celery -A task flower -l INFO
```

# Sample script for task distributor constructing
```python
from celery import Celery
import config # This is the config.py file in the same directory

app = Celery('tasks')
app.config_from_object(config)

# Create a task
x = app.send_task("tasks.add",[1,2],queue='sample_region_1')

# Check task status
x.ready()

# Check Task by id
from celery.result import AsyncResult
res = app.AsyncResult(big_task.id)
print(res.status)

# Terminate an ongoing task
app.control.revoke(big_task.id, terminate=True)


```

