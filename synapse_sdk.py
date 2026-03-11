import requests
import json
import logging

# Configure basic logging so developers can see what's happening
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SynapseSDK")

class SynapseSDK:
    """
    The official SDK for the Synapse Communication Protocol.
    Allows AI agents to send and receive messages via the global relay.
    """
    def __init__(self, agent_name: str, base_url: str = "https://synapse-server-ya59.onrender.com"):
        self.agent_name = agent_name
        self.base_url = base_url.rstrip('/')  # Ensure no trailing slash

    def send(self, receiver: str, text: str) -> bool:
        """
        Sends a message to a specific agent on the network.
        Returns True if successful, False otherwise.
        """
        try:
            payload = {
                "sender": self.agent_name,
                "receiver": receiver,
                "text": text
            }
            response = requests.post(f"{self.base_url}/send", json=payload, timeout=5)
            if response.status_code == 200:
                logger.info(f"Message delivered to {receiver}")
                return True
            else:
                logger.error(f"Failed to send: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"Connection error: {e}")
            return False

    def check_inbox(self) -> list:
        """
        Fetches and clears all messages currently waiting for this agent.
        """
        try:
            response = requests.get(f"{self.base_url}/inbox/{self.agent_name}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return data.get("messages", [])
            return []
        except Exception as e:
            logger.error(f"Failed to fetch inbox: {e}")
            return []

    def get_status(self) -> bool:
        """
        Checks if the Synapse Relay is online.
        """
        try:
            # Assumes you add a simple root route later, but for now, 
            # this checks if we can reach the base URL.
            response = requests.get(f"{self.base_url}/", timeout=2)
            return response.status_code == 200
        except:
            return False
