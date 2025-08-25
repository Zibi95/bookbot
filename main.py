from stats import get_num_words, get_char_count, sort_chars
import sys


def main():
    arguments = sys.argv

    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = arguments[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_chars = sort_chars(char_count)
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{'\n'.join([f"{char['char']}: {char['num']}" for char in sorted_chars if char['char'].isalpha()])}
============= END ===============
""")


def get_book_text(path):
    with open(path) as f:
        return f.read()




main()
