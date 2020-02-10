from kombu import Queue
## Broker settings.
BROKER_URL = 'amqp://rabbitmq_username:rabbitmq_password@rabbit_mq:5672/'

CELERY_IGNORE_RESULT = False

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "mongo_result_backend",
    "port": 27017,
    "database": "TMS_DB", 
    "taskmeta_collection": "taskmeta_collection",
    "user": 'application_user',
    "password": 'application_user_pass'
}

CELERYD_MAX_TASKS_PER_CHILD = 50

CELERY_QUEUES = {
    Queue('sample_region_1'),
    Queue('sample_region_2')
}