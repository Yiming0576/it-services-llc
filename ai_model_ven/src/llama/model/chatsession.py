import attr
from datetime import datetime
import uuid
import logging

logger = logging.getLogger(__name__)
logger.info("logger initialized.") 
@attr.s
class ChatSession:
    session_id: str = attr.ib(default=attr.Factory(lambda: uuid.uuid4().hex))
    session_name: str = attr.ib(default="Unnamed Session")
    user_input: str = attr.ib()
    chatbot_response: str = attr.ib()
    date_time: datetime = attr.ib(default=attr.Factory(datetime.now))