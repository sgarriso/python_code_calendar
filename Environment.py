import os
from dotenv import load_dotenv
class Environment:
    
    def __init__(self):
        load_dotenv()
        self.session_id = os.getenv('SESSION_ID')
        self.agent_id = os.getenv("Agent_ID")
        