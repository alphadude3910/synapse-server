import requests

# 1. Simulate Agent A sending a message
print("Agent A is sending a message...")
requests.post("http://127.0.0.1:8000/send", json={
    "sender": "Agent_A",
    "receiver": "Agent_B",
    "text": "Hello, can you hear me?"
})

# 2. Simulate Agent B checking their inbox
print("Agent B is checking for mail...")
response = requests.get("http://127.0.0.1:8000/inbox/Agent_B")
print("Response from server:", response.json())