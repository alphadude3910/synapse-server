import requests

class Synapse:
    def __init__(self, agent_name, server_url="http://127.0.0.1:8000"):
        self.agent_name = agent_name
        self.url = server_url

    def send(self, receiver, text):
        payload = {"sender": self.agent_name, "receiver": receiver, "text": text}
        requests.post(f"{self.url}/send", json=payload)

    def receive(self):
        response = requests.get(f"{self.url}/inbox/{self.agent_name}")
        return response.json().get("messages", [])