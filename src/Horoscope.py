# DSA/utils/horoscope_generator.py

"""
Horoscope Generator 🪐

This module generates random daily horoscopes for each zodiac sign.
It can be used as a standalone CLI tool or imported as a library.

Usage (Library):
    from DSA.utils.horoscope_generator import get_daily_horoscope
    print(get_daily_horoscope("Leo"))

Usage (CLI):
    python3 DSA/utils/horoscope_generator.py Leo
"""

import sys
import random
from datetime import date

# List of zodiac signs
ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Fun horoscope messages (you can add more)
MESSAGES = [
    "Today you will debug a bug that isn’t yours 🧠.",
    "Unexpected coffee ☕ may bring you the energy you need.",
    "Someone will compliment your code style. Or your hair. Or both.",
    "Take a deep breath — the error message is lying 😅.",
]