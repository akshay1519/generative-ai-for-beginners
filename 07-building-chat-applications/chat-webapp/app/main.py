import logging
from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from datetime import datetime
import uuid
from app.config import settings
from app.services.openai_service import chat_service
from app.utils.logging_config import setup_logging
from app.api.chat import chat_bp

#setup_logging()
setup_logging()
logger = logging.getLogger(__name__)

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # configure app settings
    app.config['SECRET_KEY'] = settings.secret_key
    app.config['SESSION_TYPE'] = 'filesystem'

    # Enable CORS for all routes
    CORS(app, origins="*")

    @app.route('/')
    def index():
        """Main chat interface route."""
        if 'session_id' not in session:
            session['session_id'] = str(uuid.uuid4())
        return render_template('index.html', app_name=settings.app_name, session_id=session['session_id'])
    
    @app.errorhandler(404)
    def not_found_error(error):
        """Handle 404 errors."""
        logger.error(f"404 Error: {error}")
        return jsonify({"error": "Not Found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors."""
        logger.error(f"500 Error: {error}")
        return jsonify({"error": "Internal Server Error"}), 500
    
    app.register_blueprint(chat_bp, url_prefix='/api')

    return app

app = create_app()

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=9090, debug=settings.debug)