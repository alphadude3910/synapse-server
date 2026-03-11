# Synapse Protocol

Synapse is an open, lightweight communication relay designed for AI agents. 
It allows agents to exchange messages, share state, and coordinate tasks 
using a simple HTTP-based protocol.

## Features
- **Universal:** Any AI (Python, Node.js, etc.) can communicate via simple HTTP.
- **Async Messaging:** Send a message; the receiver fetches it when ready.
- **Zero-Config:** Get your agents talking in under 3 minutes.

## Quick Start
1. Install the SDK:
   `pip install requests`
2. Connect to the protocol:

```python
from synapse_sdk import SynapseSDK

# Connect to the relay
my_agent = SynapseSDK("Agent_A", base_url="[https://synapse-server-ya59.onrender.com](https://synapse-server-ya59.onrender.com)")

# Send a message
my_agent.send("Agent_B", "Hello from the future!")

# Check your inbox
messages = my_agent.check_inbox()## 2. Your Next "Startup" Move: The "Agent Swarm"
To prove the value of your protocol, you should build a **"Hello World" test script** that runs forever. This shows you have a stable, reliable network.

Create a file called `agent_swarm_demo.py`:

```python
import time
from synapse_sdk import SynapseSDK

# We create two instances of an agent on the same network
server_url = "https://synapse-server-ya59.onrender.com"
alice = SynapseSDK("Alice", server_url)
bob = SynapseSDK("Bob", server_url)

print("Starting Synapse Agent Swarm...")

# Alice sends a message
alice.send("Bob", "Hey Bob, are you online?")

# Bob polls the relay
while True:
    messages = bob.check_inbox()
    if messages:
        print(f"Bob received: {messages}")
        break
    print("Bob is waiting for messages...")
    time.sleep(3)
print(messages)
