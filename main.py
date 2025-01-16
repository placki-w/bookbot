from collections import defaultdict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"--- Begin report of books {book_path} ---\n")
    print(f"{num_words} words found in the document.\n")
    alpha_count = character_frequency(text)
    sort_alpha_count = dict(sorted(alpha_count.items(), key=lambda item: item[1], reverse=True))
    for key, value in sort_alpha_count.items():
        if key.isalpha() == True:
            print(F"The {key} character was found {value} times.")
    print(f"\n--- End Report ---")
    
    #for key, value in alpha_count:
    print(sort_alpha_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    text_words = text.split()
    word_count = 0
    for i in text_words:
        word_count += 1
    return word_count

def character_frequency(text):
    alpha_dict = defaultdict(int)
    text_lower = text.lower()
    for i in text_lower:
        alpha_dict[i] += 1
    return alpha_dict

main()