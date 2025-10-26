"""
Feature: File Utilities
Description:
Provides basic file operations:
- Read and write .txt files
- Count number of words and lines
- Find and replace a word in a file
- Compare file hashes (MD5/SHA256) to find duplicates in a directory
"""

import os
import hashlib
from collections import defaultdict
from pathlib import Path

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


def calculate_file_hash(file_path, algorithm='md5', chunk_size=8192):
    """
    Calculate hash (MD5 or SHA256) of a file.
    
    Args:
        file_path: Path to the file
        algorithm: 'md5' or 'sha256' (default: 'md5')
        chunk_size: Size of chunks to read file in bytes (default: 8192)
    
    Returns:
        str: Hexadecimal hash string or None on error
    """
    try:
        if algorithm.lower() == 'md5':
            hash_obj = hashlib.md5()
        elif algorithm.lower() == 'sha256':
            hash_obj = hashlib.sha256()
        else:
            print(f"❌ Error: Unsupported algorithm '{algorithm}'. Use 'md5' or 'sha256'.")
            return None
        
        with open(file_path, 'rb') as file:
            while chunk := file.read(chunk_size):
                hash_obj.update(chunk)
        
        return hash_obj.hexdigest()
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"❌ Error calculating hash: {e}")
        return None


def find_duplicate_files(directory, algorithm='md5', recursive=True, min_size=0):
    """
    Find duplicate files in a directory based on their hash values.
    
    Args:
        directory: Path to the directory to scan
        algorithm: 'md5' or 'sha256' (default: 'md5')
        recursive: If True, scan subdirectories recursively (default: True)
        min_size: Minimum file size in bytes to consider (default: 0)
    
    Returns:
        dict: Dictionary mapping hashes to lists of file paths (duplicates)
    """
    if not os.path.isdir(directory):
        print(f"❌ Error: '{directory}' is not a valid directory.")
        return {}
    
    hash_to_files = defaultdict(list)
    
    print(f"🔍 Scanning directory: {directory}")
    print(f"   Algorithm: {algorithm.upper()}")
    print(f"   Recursive: {recursive}")
    print(f"   Min size: {min_size} bytes\n")
    
    # Walk through directory
    if recursive:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                _process_file(file_path, hash_to_files, algorithm, min_size)
    else:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                _process_file(file_path, hash_to_files, algorithm, min_size)
    
    # Filter to show only duplicates (files with same hash)
    duplicates = {hash_val: files for hash_val, files in hash_to_files.items() if len(files) > 1}
    
    return duplicates


def _process_file(file_path, hash_to_files, algorithm, min_size):
    """Helper function to process a single file and add to hash map."""
    try:
        # Check file size
        if os.path.getsize(file_path) < min_size:
            return
        
        # Calculate hash
        file_hash = calculate_file_hash(file_path, algorithm)
        if file_hash:
            hash_to_files[file_hash].append(file_path)
    except Exception as e:
        print(f"⚠️  Skipping '{file_path}': {e}")


def display_duplicates(directory, algorithm='md5', recursive=True, min_size=0):
    """
    Display duplicate files found in a directory.
    
    Args:
        directory: Path to the directory to scan
        algorithm: 'md5' or 'sha256' (default: 'md5')
        recursive: If True, scan subdirectories recursively (default: True)
        min_size: Minimum file size in bytes to consider (default: 0)
    
    Returns:
        dict: Dictionary mapping hashes to lists of file paths (duplicates)
    """
    duplicates = find_duplicate_files(directory, algorithm, recursive, min_size)
    
    if not duplicates:
        print("\n✅ No duplicate files found.")
        return {}
    
    print(f"\n📊 Found {len(duplicates)} set(s) of duplicate files:\n")
    
    for idx, (hash_val, files) in enumerate(duplicates.items(), 1):
        print(f"🔹 Group {idx} ({len(files)} files) - Hash: {hash_val}")
        for file in files:
            file_size = os.path.getsize(file)
            print(f"   • {file} ({file_size:,} bytes)")
        print()
    
    return duplicates


def get_file_hash_comparison(file1, file2, algorithm='md5'):
    """
    Compare two files and determine if they are identical based on hash.
    
    Args:
        file1: Path to first file
        file2: Path to second file
        algorithm: 'md5' or 'sha256' (default: 'md5')
    
    Returns:
        tuple: (are_identical: bool, hash1: str, hash2: str)
    """
    hash1 = calculate_file_hash(file1, algorithm)
    hash2 = calculate_file_hash(file2, algorithm)
    
    if hash1 is None or hash2 is None:
        return None, hash1, hash2
    
    are_identical = hash1 == hash2
    
    return are_identical, hash1, hash2


def cli_duplicate_finder():
    """Command-line interface for finding duplicate files."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Find duplicate files by comparing MD5 or SHA256 hashes'
    )
    parser.add_argument(
        'directory',
        help='Directory to scan for duplicate files'
    )
    parser.add_argument(
        '-a', '--algorithm',
        choices=['md5', 'sha256'],
        default='md5',
        help='Hash algorithm to use (default: md5)'
    )
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        default=True,
        help='Scan subdirectories recursively (default: True)'
    )
    parser.add_argument(
        '--no-recursive',
        dest='recursive',
        action='store_false',
        help='Do not scan subdirectories'
    )
    parser.add_argument(
        '-s', '--min-size',
        type=int,
        default=0,
        help='Minimum file size in bytes to consider (default: 0)'
    )
    
    args = parser.parse_args()
    
    display_duplicates(
        args.directory,
        algorithm=args.algorithm,
        recursive=args.recursive,
        min_size=args.min_size
    )


if __name__ == "__main__":
    cli_duplicate_finder()
