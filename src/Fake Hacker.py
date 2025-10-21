# DSA/fun/matrix_hack_simulator.py

"""
Matrix / Fake Hacking Log Simulator 🧠💻

This script prints random "hacking logs" or Matrix-like green text in the terminal.
It's purely for fun roleplay, has no real hacking functionality.

Usage:
    python3 DSA/fun/matrix_hack_simulator.py
"""

import random
import time
import sys
import string
import os

# Some sample fake log lines (you can add more for variety)
LOG_LINES = [
    "[ACCESS] Granted for user: root",
    "[INIT] Launching brute-force on port 22...",
    "[SCAN] Scanning subnet 192.168.0.* ...",
    "[INJECT] Payload uploaded successfully.",
    "[DECRYPT] 256-bit encryption cracked ✅",
    "[TRACE] Signal intercepted from node-42",
    "[SYS] Firewall bypass detected",
    "[MATRIX] Establishing neural handshake...",
    "[UPLOAD] Data exfiltration in progress...",
    "[LINK] Secure channel established 🛰️",
    "[ALERT] Intrusion countermeasures offline.",
    "[SHELL] Reverse shell connected from 10.0.0.1337",
    "[CODE] > Compiling quantum override patch...",
    "[PROGRESS] ████████▒▒▒▒▒▒ 67%",
    "[SUCCESS] Operation completed successfully.",
]

# Matrix-style characters
MATRIX_CHARS = string.ascii_letters + string.digits + string.punctuation

def print_matrix_line(width=80):
    """Print a line of random green 'Matrix' characters."""
    line = "".join(random.choice(MATRIX_CHARS) for _ in range(width))
    print(f"\033[92m{line}\033[0m")  # Green text

def print_fake_log():
    """Print a random fake hacking log line with slight delay."""
    line = random.choice(LOG_LINES)
    print(f"\033[92m{line}\033[0m")  # Green
    time.sleep(random.uniform(0.05, 0.3))

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("\033[92mInitializing Matrix sequence...\033[0m")
    time.sleep(1)

    try:
        while True:
            # Randomly choose between matrix line or fake log
            if random.random() < 0.7:
                print_matrix_line(random.randint(50, 100))
            else:
                print_fake_log()
            time.sleep(random.uniform(0.02, 0.15))
    except KeyboardInterrupt:
        print("\n\033[91m[EXIT] Matrix simulation terminated.\033[0m")
        sys.exit(0)


if __name__ == "__main__":
    main()
