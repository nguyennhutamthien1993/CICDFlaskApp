from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Wait between 1 and 3 seconds
    @task
    def index_page(self):
        self.client.get("/")