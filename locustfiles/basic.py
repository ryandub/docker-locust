from locust import Locust, TaskSet, task
import os

class MyTaskSet(TaskSet):
    @task(2)
    def index(self):
        self.client.get("/")

class MyLocust(Locust):
    host = os.environ['host']
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
