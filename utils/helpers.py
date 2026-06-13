import os, sys, time
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def print_colored(text, color="white", bold=False):
    color_map = {"red": Fore.RED, "green": Fore.GREEN, "yellow": Fore.YELLOW, "blue": Fore.BLUE, "cyan": Fore.CYAN, "white": Fore.WHITE, "magenta": Fore.MAGENTA}
    style = Style.BRIGHT if bold else ""
    print(f"{style}{color_map.get(color.lower(), Fore.WHITE)}{text}{Style.RESET_ALL}")

def print_typing_indicator(duration=1.0, message="Thinking"):
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    idx = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{Fore.CYAN}{animation[idx % len(animation)]} {message}...")
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')

def format_timestamp(): return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def print_banner():
    banner = """
    ╔═══════════════════════════════════════════╗
    ║        🤖  AI CHATBOT ASSISTANT  🤖       ║
    ╚═══════════════════════════════════════════╝"""
    print_colored(banner, "cyan", bold=True)

def print_help():
    print_colored("\nCommands: /help, /clear, /history, /quit (or exit, bye)\n", "yellow")
