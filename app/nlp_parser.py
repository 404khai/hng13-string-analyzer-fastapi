def parse_query(query: str):
    q = query.lower().strip()
    filters = {}

    if "palindromic" in q:
        filters["is_palindrome"] = True
    if "single word" in q:
        filters["word_count"] = 1
    if "longer than" in q:
        words = q.split()
        try:
            idx = words.index("than")
            filters["min_length"] = int(words[idx + 1]) + 1
        except:
            raise ValueError("Cannot parse length condition")
    if "containing the letter" in q:
        idx = q.index("containing the letter")
        char = q[idx + len("containing the letter"):].strip().split()[0]
        filters["contains_character"] = char
    if not filters:
        raise ValueError("Unable to parse natural language query")
    return filters
