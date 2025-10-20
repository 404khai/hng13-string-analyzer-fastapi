import hashlib
from collections import Counter

def analyze_string(value: str):
    clean_value = value.strip()
    lower_value = clean_value.lower()  # normalize for analysis

    sha_hash = hashlib.sha256(clean_value.encode()).hexdigest()

    # frequency map should be case-insensitive
    char_map = dict(Counter(ch for ch in lower_value if not ch.isspace()))

    # palindrome check (case-insensitive, ignoring spaces)
    cleaned_for_palindrome = ''.join(ch.lower() for ch in clean_value if ch.isalnum())
    is_palindrome = cleaned_for_palindrome == cleaned_for_palindrome[::-1]

    # unique chars count (case-insensitive)
    unique_chars = len(set(lower_value.replace(" ", "")))

    # word count (split by whitespace)
    words = len(clean_value.split())

    return {
        "length": len(clean_value),
        "is_palindrome": is_palindrome,
        "unique_characters": unique_chars,
        "word_count": words,
        "sha256_hash": sha_hash,
        "character_frequency_map": char_map
    }
