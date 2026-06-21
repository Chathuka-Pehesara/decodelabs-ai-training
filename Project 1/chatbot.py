import sys
from typing import Dict, List, Tuple

# ANSI Color palette constants
COLOR_THEME: Dict[str,str] = {
    "BOT": "\033[96m",
    "SYSTEM": "\033[93m",
    "USER": "\033[97m",
    "RESET": "\033[0m"
}

def print_banner() -> None:
    border = "=" * 60
    title = "CPBOT (v1.0.0)"
    tagline = "A portfolio-Grade Rule-based AI Chatbot for DecodeLabs"

    print(f"{COLOR_THEME['SYSTEM']}{border}")
    print(f"{title:^60}")
    print(f"{tagline:^60}")
    print(f"{border}{COLOR_THEME['RESET']}\n")
    print(f"{COLOR_THEME['SYSTEM']}System: Type 'help' to see what I can do or 'exit' to quit.{COLOR_THEME['RESET']}\n")
    
print_banner()