import attr
import uuid
from datetime import datetime

@attr.s
class ChatSession:
    session_id: str = attr.ib(default=attr.Factory(lambda: uuid.uuid4().hex))
    user_id: str = attr.ib(default=None)  # Optionally link to a specific user
    user_input: str = attr.ib()
    chatbot_response: str = attr.ib()
    create_time: datetime = attr.ib(default=attr.Factory(datetime.now))
    end_time: datetime = attr.ib(default=None)  # Optional: When the session ended
    session_duration: float = attr.ib(default=None)  # Duration of the session in seconds
    language: str = attr.ib(default='en')  # Language used in the chat
    feedback: str = attr.ib(default=None)  # Optional user feedback on the chatbot response
    context: dict = attr.ib(factory=dict)  # Context or metadata related to the session
    
    def update_end_time(self):
        """Update the end time and calculate session duration."""
        self.end_time = datetime.now()
        if self.end_time and self.create_time:
            self.session_duration = (self.end_time - self.create_time).total_seconds()
