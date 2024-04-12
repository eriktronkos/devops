import time
from locust import HttpUser, task, between
from random import choice

class LoadTest(HttpUser):
    wait_time = between(1, 2)
    todo_ids = [1]

    @task(3)
    def list(self):
        self.client.get("/api/v1/todos/")

    @task(3)
    def get(self):
        self.client.get(f"/api/v1/todos/{choice(self.todo_ids)}/")

    @task(1)
    def post(self):
        response = self.client.post(f"/api/v1/todos/", json={"title": "foo", "description": "bar"})
        response_data = response.json()
        self.todo_ids.append(response_data["id"])