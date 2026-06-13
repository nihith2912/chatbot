import traceback
from chatbot import Chatbot
from config import Config
from utils.helpers import print_colored, print_banner, print_help, clear_screen
from colorama import Fore, Style

def main():
    try:
        if not Config.validate():
            raise ValueError("Invalid configuration. Check .env file.")

        bot = Chatbot()
        clear_screen()
        print_banner()
        print_colored("Welcome! Type '/help' for commands.\n", "cyan")

        while True:
            try:
                user_input = input(
                    f"\n{Style.BRIGHT}{Fore.GREEN}You: {Style.RESET_ALL}"
                ).strip()

                if not user_input:
                    continue

                cmd = user_input.lower()

                if cmd in ['/quit', 'quit', 'exit', 'bye']:
                    print_colored("\n👋 Goodbye!", "cyan", bold=True)
                    break

                elif cmd == '/help':
                    print_help()

                elif cmd == '/clear':
                    bot.clear_history()
                    print_colored("✓ Cleared", "green")

                elif cmd == '/history':
                    bot.display_history()

                elif cmd.startswith('/'):
                    print_colored("Unknown command. Type /help", "yellow")

                else:
                    response = bot.get_response(user_input)
                    print_colored(f"\nBot: {response}", "blue")

            except (KeyboardInterrupt, EOFError):
                print_colored("\n\n👋 Goodbye!", "cyan")
                break

    except Exception:
        print("\nFULL ERROR TRACEBACK:\n")
        traceback.print_exc()

if __name__ == "__main__":
    main()