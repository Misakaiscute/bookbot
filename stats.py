def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()

def get_num_words(file_as_text: str) -> int:
    words = file_as_text.split()
    return len(words)

def get_num_letters_in_text(file_as_text: str) -> dict[str, int]:
    res = dict()
    for letter in file_as_text:
        letter_lower = letter.lower()
        if letter_lower not in res:
            res[letter_lower] = 1
        else:
            res[letter_lower] += 1
    return res

def sort_on_letter_occourance(dict: dict[str, int]) -> list[dict[str, int]]:
    res_list = []
    for entry in dict:
        entry_dict = {}
        entry_dict["char"] = entry
        entry_dict["num"] = dict[entry]
        res_list.append(entry_dict)

    res_list.sort(reverse=True, key=(lambda entry : entry["num"]))
    return res_list