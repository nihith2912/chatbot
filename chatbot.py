from datetime import datetime
from config import Config
from utils.logger import setup_logger
from utils.helpers import print_typing_indicator, print_colored

logger = setup_logger(
    log_level=Config.LOG_LEVEL,
    enable_logging=Config.ENABLE_LOGGING
)


class ChatMessage:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "role": self.role,
            "content": self.content
        }


class GeminiProvider:
    def __init__(self):
        import google.generativeai as genai

        genai.configure(api_key=Config.GEMINI_API_KEY)

        self.model = genai.GenerativeModel("gemini-2.5-flash")
        self.chat = None

    def generate_response(self, messages):
        if not self.chat:
            self.chat = self.model.start_chat(history=[])

        response = self.chat.send_message(
            messages[-1]["content"]
        )

        return response.text

    def reset_chat(self):
        self.chat = None


class Chatbot:
    def __init__(self):
        self.history = [
            ChatMessage(
                "system",
                "You are a helpful AI assistant."
            )
        ]

        self.provider = GeminiProvider()

    def get_response(self, user_input: str) -> str:
        self.history.append(
            ChatMessage("user", user_input)
        )

        if len(self.history) > Config.MAX_HISTORY_LENGTH + 1:
            self.history = (
                [self.history[0]]
                + self.history[-Config.MAX_HISTORY_LENGTH:]
            )

        try:
            print_typing_indicator(0.5)

            response = self.provider.generate_response(
                [msg.to_dict() for msg in self.history]
            )

            self.history.append(
                ChatMessage("assistant", response)
            )

            return response

        except Exception as e:
            logger.error(f"Error: {e}")
            return f"Error occurred: {str(e)}"

    def clear_history(self):
        self.history = [self.history[0]]
        self.provider.reset_chat()

    def display_history(self):
        for msg in self.history[1:]:
            color = "green" if msg.role == "user" else "blue"
            prefix = "You" if msg.role == "user" else "Bot"

            print_colored(
                f"[{msg.timestamp}] {prefix}: {msg.content}",
                color
            )