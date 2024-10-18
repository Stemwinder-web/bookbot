def main():
    book_path = "books/frankenstein.txt"  
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counter = get_characters(text)
    listed_char = chars_dict_to_sorted_list(character_counter)
   
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for my_letters in listed_char:
        if not my_letters["char"].isalpha():
            continue
        print(f"the'{my_letters['char']}'character was found {my_letters['num']}times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_characters(text):
    chars ={}
    for c in text:
        TRUE_string = c.lower()
        if TRUE_string in chars:
            chars[TRUE_string] += 1
        else:
            chars[TRUE_string] = 1
    return chars
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()