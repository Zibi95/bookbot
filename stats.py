def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text: str) -> dict[str, int]:
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_chars(chars: dict[str, int]) -> list[dict[str, int]]:
    list = []
    for char, count in chars.items():
        list.append({'char': char, 'num': count})
    return sorted(list, key=lambda x: x['num'], reverse=True)