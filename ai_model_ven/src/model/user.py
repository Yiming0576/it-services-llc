import attr
import uuid
from datetime import datetime
from typing import List
from .record import Record
from .person import Person
from .chatsession import ChatSession



@attr.s
class User(Person):
    """A class representing a user in the system.
    
    Attributes:
        user_id (str): The unique identifier for the user.
        email (str): The email address of the user.
        password_hash (str): The hashed password of the user.
        created_at (datetime): The timestamp when the user was created.
        updated_at (datetime): The timestamp when the user was last updated.
        profile_picture_url (str): The URL of the user's profile picture.
        is_active (bool): Indicates whether the user is active or not.
        last_login (datetime): The timestamp of the user's last login.
        roles (List[str]): The list of roles assigned to the user.
        chat_record (Record): The record of chat sessions associated with the user.
    """
    
    user_id: str = attr.ib(default=attr.Factory(lambda: uuid.uuid4().hex))
    email: str = attr.ib()
    password_hash: str = attr.ib()
    created_at: datetime = attr.ib(default=attr.Factory(datetime.now))
    updated_at: datetime = attr.ib(default=attr.Factory(datetime.now))
    profile_picture_url: str = attr.ib(default=None)
    is_active: bool = attr.ib(default=True)
    last_login: datetime = attr.ib(default=None)
    roles: List[str] = attr.ib(factory=list)
    
    chat_record: Record = attr.ib(factory=Record)

    def update_last_login(self):
        """Update the last login time to the current time."""
        self.last_login = datetime.now()
        self.updated_at = datetime.now()
    
    def update_profile(self, profile_picture_url=None):
        """Update user's profile information.
        
        Args:
            profile_picture_url (str, optional): The URL of the updated profile picture.
        """
        if profile_picture_url is not None:
            self.profile_picture_url = profile_picture_url
        self.updated_at = datetime.now()

    def add_chat_session(self, session: ChatSession):
        """Add a chat session to the user's record.
        
        Args:
            session (ChatSession): The chat session to be added.
        """
        session.user_id = self.user_id 
        self.chat_record.add_session(session)
    
    def get_chat_session(self, session_id: str) -> ChatSession:
        """Retrieve a specific chat session by its ID.
        
        Args:
            session_id (str): The ID of the chat session to retrieve.
        
        Returns:
            ChatSession: The chat session with the specified ID.
        """
        return self.chat_record.get_session_by_id(session_id)
    
    def get_all_chat_sessions(self) -> List[ChatSession]:
        """Retrieve all chat sessions associated with the user.
        
        Returns:
            List[ChatSession]: A list of all chat sessions associated with the user.
        """
        return self.chat_record.get_all_sessions()
    
    def remove_chat_session(self, session_id: str):
        """Remove a chat session by its ID.
        
        Args:
            session_id (str): The ID of the chat session to remove.
        """
        self.chat_record.remove_session_by_id(session_id)