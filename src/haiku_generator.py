import random

THEMED_WORD_BANKS = {
    'nature': {
        '5': [
            "Autumn leaves falling",
            "Crimson sunset glow",
            "Waves kiss the shoreline",
            "Silent moon above",
            "Cherry blossoms bloom",
        ],
        '7': [
            "Whispers of the morning breeze",
            "Mountains touch the endless sky",
            "River flows without a sound",
            "Echoes of a distant drum",
            "Petals drift on silent streams",
        ],
    },

    'love': {
        '5': [
            "Warmth in gentle touch",
            "Heartbeat softly beats",
            "Eyes full of passion",
            "Sweet whispers at dusk",
            "Tenderness remains",
        ],
        '7': [
            "Love blooms beneath the starlit sky",
            "Promises whispered on the breeze",
            "Moments linger in the soft light",
            "Holding hands through endless nights",
            "Songs carry feelings deep within",
        ],
    },

    'season': {
        '5': [
            "Snowflakes kiss the earth",
            "Spring blooms in colors bright",
            "Summer sun above",
            "Leaves fall silently",
            "Winter winds grow cold",
        ],
        '7': [
            "Breeze carries scents of fresh blossoms",
            "Frost glistens on morning grass",
            "Thunder shakes the summer sky",
            "Rain taps on the windowpane",
            "Nature sleeps in cold embrace",
        ],
    }
}

DEFAULT_THEME = 'nature'


def generate_haiku_with_theme(theme):
    theme = theme.lower()
    if theme not in THEMED_WORD_BANKS:
        theme = DEFAULT_THEME

    five_syllable_lines = THEMED_WORD_BANKS[theme]['5']
    seven_syllable_lines = THEMED_WORD_BANKS[theme]['7']

    line1 = random.choice(five_syllable_lines)
    line2 = random.choice(seven_syllable_lines)
    line3 = random.choice(five_syllable_lines)

    return f"{line1}\n{line2}\n{line3}"


def main():
    print("Welcome to the Themed Haiku Generator!")
    print("Available themes: nature, love, season")
    user_theme = input("Please enter a theme: ")

    haiku = generate_haiku_with_theme(user_theme)
    print("\nHere is your themed haiku:\n")
    print(haiku)


if __name__ == '__main__':
    main()
