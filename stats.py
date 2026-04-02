# Function to access the books contents
def get_book_text(file_path):
   with open(file_path) as file:
       file_contents = file.read()
    
   return file_contents

# Function to count the words
def count_book_words(text):
    text_book = get_book_text(text)
    words = text_book.split()
    count_words = len(words)
    return count_words

def count_book_char(text):
    text_book = get_book_text(text)
    text_book_lower = text_book.lower()

    counted = {}
    for char in text_book_lower:
        if char not in counted:
            counted[char] = 1
        else:
            counted[char] += 1
    
    return counted

def sorted_dict_helper(text):
    return text["num"]

def sorted_list_dict(char_count):
    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key=sorted_dict_helper, reverse=True)
    return char_list



    


