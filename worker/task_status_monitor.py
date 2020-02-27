from celery import Celery
import config # This is the config.py file in the same directory

app = Celery('tasks')
app.config_from_object(config)
# x = app.send_task("tasks.add",[1,2],queue='sample_region_1')
# x.ready()


# Terminate a task

# big_task = app.send_task('tasks.big_task', [10], queue='sample_region_1')
# print('Big Task ID:' ,big_task.id)
# app.control.revoke(big_task.id, terminate=True)

# res = app.AsyncResult(big_task.id)
# print(res.status)

for i in range(100):
    app.send_task('tasks.big_task', [10], queue='sample_region_1')

print("Done sending all tasks")