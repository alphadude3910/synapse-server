from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# This is where we hold the mail until an agent picks it up
storage = {} 

class Message(BaseModel):
    sender: str
    receiver: str
    text: str

@app.post("/send")
def send_message(msg: Message):
    if msg.receiver not in storage:
        storage[msg.receiver] = []
    storage[msg.receiver].append(msg)
    return {"status": "Message stored"}

@app.get("/inbox/{agent_name}")
def get_inbox(agent_name: str):
    return {"messages": storage.pop(agent_name, [])}