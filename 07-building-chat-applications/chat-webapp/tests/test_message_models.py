from app.models.message import Message, Conversation
from datetime import datetime

def test_message_creation():
    msg = Message(role="user", content="Hello!")
    assert msg.role == "user"
    assert msg.content == "Hello!"
    assert isinstance(msg.timestamp, datetime)

def test_conversation_add_and_get_messages():
    conv = Conversation(session_id="test123")
    msg1 = Message(role="user", content="Hi")
    msg2 = Message(role="assistant", content="Hello!")
    conv.add_message(msg1)
    conv.add_message(msg2)
    assert len(conv.messages) == 2
    api_msgs = conv.get_messages_for_api()
    print(api_msgs)
    assert api_msgs == [
        {"role": "user", "content": "Hi", "timestamp": msg1.timestamp.isoformat()},
        {"role": "assistant", "content": "Hello!", "timestamp": msg2.timestamp.isoformat()},
    ]
    last_msgs = conv.get_last_message(1)
    assert last_msgs[0].content == "Hello!"