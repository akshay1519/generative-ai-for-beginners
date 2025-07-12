from flask import Blueprint, request, jsonify, session
from app.services.openai_service import chat_service

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()
    temperature = float(data.get('temperature', 0.7))
    if not user_message:
        return jsonify({'response': 'Please enter a message.'}), 400

    # Build the conversation (system + user message)
    system_msg = chat_service.create_system_message()
    messages = [system_msg, {"role": "user", "content": user_message}]
    try:
        response = chat_service.get_chat_response(messages, temperature=temperature)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': 'Error: Unable to get response.'}), 500
