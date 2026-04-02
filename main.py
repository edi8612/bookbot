import sys
from stats import count_book_words, count_book_char, sorted_list_dict


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    num_words = count_book_words(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_count = count_book_char(book_path)

    sorted_char_list = sorted_list_dict(char_count)
    
    for char_dict in sorted_char_list:
        print(f"{char_dict['char']}: {char_dict['num']}")

    print("============= END ===============")

    

main()