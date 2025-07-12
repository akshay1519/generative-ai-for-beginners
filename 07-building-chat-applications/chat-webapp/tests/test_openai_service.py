import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from app.services.openai_service import chat_service

def test_aoai_connection():
    print("Testing Azure OpenAI connection...")
    try:
        # Create a simple system message and user message
        system_msg = chat_service.create_system_message()
        messages = [
            system_msg,
            {"role": "user", "content": "Hello, are you there?"}
        ]
        # Try to get a response from AOAI
        response = chat_service.get_chat_response(messages)
        assert response and isinstance(response, str)
        print("AOAI connection established and response received.")
        print("Sample response:", response[:200])
    except Exception as e:
        print("AOAI connection test failed:", e)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_aoai_connection()