import sys
from stats import get_book_text, get_num_words, get_num_letters_in_text, sort_on_letter_occourance

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_contents = get_book_text(sys.argv[-1])
        words_count = get_num_words(file_contents)
        print(f"Found {words_count} total words")

        dict = get_num_letters_in_text(file_contents)
        list_of_dicts_sorted = sort_on_letter_occourance(dict)
        for char_data in list_of_dicts_sorted:
            if char_data["char"].isalpha():
                print(f"{char_data["char"]}: {char_data["num"]}")
main()