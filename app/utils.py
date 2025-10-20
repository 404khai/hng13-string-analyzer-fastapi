import hashlib
from collections import Counter

def analyze_string(value: str):
    clean_value = value.strip()
    sha_hash = hashlib.sha256(clean_value.encode()).hexdigest()
    char_map = dict(Counter(clean_value))
    is_palindrome = clean_value.lower() == clean_value[::-1].lower()
    unique_chars = len(set(clean_value))
    words = len(clean_value.split())

    return {
        "length": len(clean_value),
        "is_palindrome": is_palindrome,
        "unique_characters": unique_chars,
        "word_count": words,
        "sha256_hash": sha_hash,
        "character_frequency_map": char_map
    }
