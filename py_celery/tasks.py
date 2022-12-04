from celery import Celery
from time import sleep
app = Celery('tasks', backend="rpc://", broker='amqp://guest@localhost//')

@app.task
def reverse(text):
    sleep(5)
    return text[::-1]
# $ docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 rabbitmq:3-management
# $ docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 rabbitmq:3-management