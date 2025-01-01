def readout(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        print(file_content)
        
def get_word_count(path_to_file):
    word_count = 0
    with open(path_to_file) as f:
        words = f.read()
        for word in words.split():
            word_count += 1
    return word_count

def get_char_count(path_to_file):
    result_dict = {}
    result_list = []
    with open(path_to_file) as f:
        file = f.read()
        lowered_file = file.lower()
        for char in lowered_file:
            if char in result_dict:
                result_dict[char] += 1
            else:
                result_dict[char] = 1
    for key in result_dict:
        if key.isalpha():
            temp = {"char": key, "count": result_dict[key]}
            result_list.append(temp)
    return result_list

def sort_on_frequency(dict):
    return dict["count"]

def report_word_char(bookpath):
    word_count = get_word_count(bookpath)
    char_list = get_char_count(bookpath)
    print(word_count)
    char_list.sort(reverse=True, key=sort_on_frequency)
    print(f"--- Begin report of {bookpath}")
    print(f"{word_count} words were found in the document\n")
    print("")
    for item in char_list:
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    print("--- End report ---")

def main():
    book_filepath = "books/frankenstein.txt"
    report_word_char(book_filepath)


main()