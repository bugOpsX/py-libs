"""
Feature: File Utilities
Description:
Provides basic file operations:
- Read and write .txt files
- Count number of words and lines
- Find and replace a word in a file
"""

def read_file(file_path):
    """Read and return the contents of a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
        return None


def write_file(file_path, content):
    """Write text content to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✅ Successfully written to '{file_path}'.")
    except Exception as e:
        print(f"❌ Error writing to file: {e}")


def count_words_and_lines(file_path):
    """Count and return the number of words and lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            return {
                "lines": len(lines),
                "words": word_count
            }
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
        return None


def find_and_replace(file_path, old_word, new_word):
    """Find and replace a word in a file (case-sensitive)."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        updated_content = content.replace(old_word, new_word)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        print(f"✅ Replaced '{old_word}' with '{new_word}' in '{file_path}'.")
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
