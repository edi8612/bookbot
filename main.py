from stats import count_book_words

def main():
    num_words = count_book_words("books/frankenstein.txt")

    print(f"Found {num_words} total words")

main()