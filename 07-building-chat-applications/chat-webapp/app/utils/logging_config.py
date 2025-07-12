import logging
import sys
from app.config import settings

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Set Azure SDK logging to WARNING to reduce noise
    logging.getLogger('azure').setLevel(logging.WARNING)
    logging.getLogger('azure.identity').setLevel(logging.INFO)
    logging.getLogger('azure.core').setLevel(logging.WARNING)