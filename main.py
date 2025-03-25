from stats import get_num_words
from stats import count_chars
from stats import report
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

    
def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Count the words
    word_count = get_num_words(book_text)
    print(f"Word count: {word_count}")

    # Count the characters
    char_counts = count_chars(book_text)
        
    report(word_count,char_counts)
    
main()

