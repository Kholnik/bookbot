def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    chars = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char.isalpha():  # only count letters
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_characters(text)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    # Create list of dictionaries
    char_list = []
    for char, count in chars.items():
        char_dict = {'char': char, 'num': count}
        char_list.append(char_dict)

    # Sort the list
    char_list.sort(reverse=True, key=sort_on)

    # Print each character's count
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    main()