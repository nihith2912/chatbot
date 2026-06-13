"""Configuration module for the AI Chatbot."""
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_PROVIDER: str = os.getenv("API_PROVIDER", "openai").lower()
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    OPENAI_MAX_TOKENS: int = int(os.getenv("OPENAI_MAX_TOKENS", "150"))
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    
    GEMINI_API_KEY: Optional[str] = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-pro")
    GEMINI_TEMPERATURE: float = float(os.getenv("GEMINI_TEMPERATURE", "0.7"))
    
    MAX_HISTORY_LENGTH: int = int(os.getenv("MAX_HISTORY_LENGTH", "10"))
    ENABLE_LOGGING: bool = os.getenv("ENABLE_LOGGING", "True").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate(cls) -> bool:
        if cls.API_PROVIDER == "openai": return bool(cls.OPENAI_API_KEY)
        if cls.API_PROVIDER == "gemini": return bool(cls.GEMINI_API_KEY)
        return False

if not Config.validate():
    raise ValueError(f"Invalid configuration for provider: {Config.API_PROVIDER}")
