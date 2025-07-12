from datetime import datetime, timezone
from typing import List
from pydantic import BaseModel, Field

class Message(BaseModel):
    """ Chat message model. """
    role: str = Field(..., description="Role of the message sender (e.g., 'user', 'assistant')")
    content: str = Field(..., description="Content of the message")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of when the message was created")

    def dict(self):
        return {
            "role": self.role,
            "content": self.content,
            "timestamp": self.timestamp.isoformat()
        }

class Conversation(BaseModel):
    """ Conversation model  """
    session_id: str = Field(..., description="Unique identifier for the conversation session")
    messages: List[Message] = Field(default_factory=list, description="List of messages in the conversation")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of when the conversation was created")

    def add_message(self, message: Message):
        """ Add a message to the conversation. """
        self.messages.append(message)
    
    def get_messages_for_api(self):
        """ Get messages formatted for API response. """
        return [{"role": msg.role, "content": msg.content, "timestamp": msg.timestamp.isoformat()} for msg in self.messages]
    
    def get_last_message(self, count: int = 1):
        """ Get the last `count` messages in the conversation. """
        return self.messages[-count:] if len(self.messages) >= count else self.messages