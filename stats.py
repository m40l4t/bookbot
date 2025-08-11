def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text: str) -> dict[str, int]:
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts: dict[str, int]) -> list[dict[str, int]]:
    items = [{"char": ch, "num": count} for ch, count in char_counts.items()]
    items.sort(key=lambda d: d["num"], reverse=True)
    return items
    
