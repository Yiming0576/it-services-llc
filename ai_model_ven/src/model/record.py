import attr
from typing import List
from .chatsession import ChatSession
from typing import List

@attr.s
class Record:
    """A record that stores chat sessions."""
    
    sessions: List[ChatSession] = attr.ib(factory=list)
    user_id: str = attr.ib(default=None)
    
    def add_session(self, session: ChatSession):
        """Add a new chat session to the record.
        
        Args:
            session (ChatSession): The chat session to be added.
        """
        self.sessions.append(session)
    
    def get_session_by_id(self, session_id: str) -> ChatSession:
        """Retrieve a chat session by its session ID.
        
        Args:
            session_id (str): The ID of the chat session to retrieve.
        
        Returns:
            ChatSession: The chat session with the specified ID, or None if not found.
        """
        for session in self.sessions:
            if session.session_id == session_id:
                return session
        return None  # Or raise an exception if preferred
    
    def get_all_sessions(self) -> List[ChatSession]:
        """Return a list of all chat sessions.
        
        Returns:
            List[ChatSession]: A list of all chat sessions.
        """
        return self.sessions
    
    def remove_session_by_id(self, session_id: str):
        """Remove a chat session by its session ID.
        
        Args:
            session_id (str): The ID of the chat session to remove.
        """
        self.sessions = [session for session in self.sessions if session.session_id != session_id]
