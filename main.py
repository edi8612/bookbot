
# Function to access the books contents
def get_book_text(file_path):
   with open(file_path) as file:
       file_contents = file.read()
    
   return file_contents


def count_book_words(text):
    text_book = get_book_text(text)
    words = text_book.split()
    count_words = len(words)
    return count_words

def main():
    num_words = count_book_words("books/frankenstein.txt")

    print(f"Found {num_words} total words")

main()