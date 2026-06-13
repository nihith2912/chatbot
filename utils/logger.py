import logging
import os
from datetime import datetime
from pathlib import Path

def setup_logger(name="chatbot", log_level="INFO", enable_logging=True):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    logger.handlers.clear()
    
    if not enable_logging:
        logger.addHandler(logging.NullHandler())
        return logger
        
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    
    file_handler = logging.FileHandler(logs_dir / f"chatbot_{datetime.now().strftime('%Y%m%d')}.log", encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
