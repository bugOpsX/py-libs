# DSA/utils/roast_generator.py

"""
Light-Hearted Roast Generator 🔥

This module generates playful roasts or jokes.
It has a safe/family-friendly mode to keep it clean.

Usage (Library):
    from DSA.utils.roast_generator import get_roast
    print(get_roast())  # Random roast
    print(get_roast(family_friendly=True))  # Safe roast

Usage (CLI):
    python3 DSA/utils/roast_generator.py [safe]
    safe: optional, "yes" for family-friendly mode
"""

import random
import sys

# Regular playful roasts
ROASTS = [
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You have something on your chin… no, the third one down.",
    "You bring everyone so much joy… when you leave the room.",
    "You're proof that even evolution takes breaks sometimes.",
    "You're like a software update… whenever I see you, I think 'Do I really need this now?'",
    "You're the human version of a typo.",
    "You're like a cloud storage service — nobody remembers your password."
]

# Family-friendly / safe roasts
SAFE_ROASTS = [
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You're so bright, you could be a lighthouse!",
    "You're like a puppy — adorable but a little clumsy sometimes.",
    "You bring smiles wherever you go.",
    "You're like a WiFi signal — strong when it counts.",
    "You're like a sunny day — hard not to like you.",
    "You're unique… like a one-of-a-kind sticker!"
]

# Small improvement: simple mapping for easy management
_ROAST_SETS = {
    "regular": ROASTS,
    "safe": SAFE_ROASTS,
    "family": SAFE_ROASTS
}

def get_roast(family_friendly=False):
    """
    Return a random roast.
    :param family_friendly: bool - If True, use safe roasts
    """
    if family_friendly:
        return random.choice(SAFE_ROASTS)
    return random.choice(ROASTS)


def cli():
    """Command-line interface for roast generator."""
    family_friendly = False

    # Enhancement: handle more safe-mode keywords
    if len(sys.argv) == 2:
        arg = sys.argv[1].lower()
        if arg in ["yes", "true", "1", "safe", "family"]:
            family_friendly = True
        elif arg not in _ROAST_SETS:
            print("Usage: python3 DSA/utils/roast_generator.py [safe|yes|true|1|family]")
            return

    roast = get_roast(family_friendly)
    print(f"🔥 Roast: {roast}")


if __name__ == "__main__":
    cli()
