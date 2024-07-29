import attr
import uuid
from datetime import datetime

@attr.s
class ChatSession:
    """
    Represents a chat session with various attributes capturing details about the session.
    """
    session_id: str = attr.ib(default=attr.Factory(lambda: uuid.uuid4().hex))
    user_input: dict = attr.ib(default=None)
    chatbot_response: str = attr.ib(default=None)
    create_time: datetime = attr.ib(default=attr.Factory(datetime.now))
    end_time: datetime = attr.ib(default=None)  
    session_duration: float = attr.ib(default=None) 
    language: str = attr.ib(default='en')  
    feedback: str = attr.ib(default=None)  
    context: dict = attr.ib(default=None) 
    conversation_history: list = attr.ib(default=None)


    def end_session(self):
        """
        Marks the end of the session and calculates the duration.
        """
        self.end_time = datetime.now()
        self.calculate_duration()

    def calculate_duration(self):
        """
        Calculates the duration of the session if both start and end times are available.
        """
        if self.create_time and self.end_time:
            self.session_duration = (self.end_time - self.create_time).total_seconds()

    def update_feedback(self, feedback):
        """
        Updates the feedback for the chatbot response.
        
        Args:
            feedback (str): The feedback provided by the user.
        """
        self.feedback = feedback
