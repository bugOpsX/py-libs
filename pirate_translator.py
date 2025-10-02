"""
this script converts normal english text into pirate-style english
"""

import re
import sys
from typing import Dict

# word mapping
word_map: Dict[str, str] = {
    "hello": "ahoy",
    "hi": "yo-ho-ho",
    "my": "me",
    "friend": "matey",
    "friends": "mateys",
    "is": "be",
    "are": "be",
    "the": "th’",
    "you": "ye",
    "your": "yer",
    "sir": "cap’n",
    "madam": "proud lady",
    "where": "whar",
    "stop": "avast",
    "yes": "aye",
    "no": "nay",
    "money": "booty",
    "treasure": "booty",
    "left": "port",
    "right": "starboard",
    "old": "barnacle-covered",
    "to": "t’",
    "island": "isle",
}

# extra pirate words
interjections = ("Arr!", "Yarr!", "Argh!", "Aye!")


def preserve_case(src: str, dst: str) -> str:
    # match the word case
    if src.isupper():
        return dst.upper()
    if src[0].isupper():
        return dst.capitalize()
    return dst


def replace_words(text: str, mapping: Dict[str, str]) -> str:
    # replace full words only
    def repl(m: re.Match) -> str:
        word = m.group(0)
        low = word.lower()
        if low in mapping:
            return preserve_case(word, mapping[low])
        return word
    return re.sub(r"\b[\w']+\b", repl, text)


def decorate(text: str) -> str:
    # add pirate touch after first sentence or exclamation
    parts = re.split(r"(\.|\?|!)", text)
    out = []
    idx = 0
    sent = 0

    for i in range(0, len(parts), 2):
        chunk = parts[i]
        punc = parts[i + 1] if i + 1 < len(parts) else ""
        piece = chunk + punc
        if punc in {".", "!"}:
            interj = interjections[idx % len(interjections)]
            if punc == "!" or sent == 0:
                piece = chunk.strip() + punc + " " + interj
                idx += 1
            sent += 1
        out.append(piece)
    return "".join(out)


def to_pirate(text: str) -> str:
    # main function
    text = replace_words(text, word_map)
    text = decorate(text)
    return text


def cli():
    # simple cli
    if len(sys.argv) < 2:
        print('usage: python3 DSA/utils/pirate_translator.py "your text here"')
        sys.exit(1)
    print(to_pirate(" ".join(sys.argv[1:])))


if __name__ == "__main__":
    cli()

