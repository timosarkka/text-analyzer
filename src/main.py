# This is a small python program that reads in a user-defined .txt-file and analyzes the contents
# It prints out a report (to terminal) that lists the word count, number of different letters and number of different words

# A function that counts the total and percentage share of different words from the contents of the file
def count_words(book_contents):
    word_list = book_contents.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict, len(word_list)

# A function that counts the letters from the contents of the file
def count_letters(book_contents):
    letter_dict = {}
    book_contents = book_contents.lower()
    for char in book_contents:
        if char in letter_dict.keys():
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict

# A helper function for the .sort() method used in the main program
def sort_on(dict):
    return dict["num"]

# A helper function that converts the letter dictionary to a list of dictionaries for sorting purposes
def dict_to_listdict(dict):
    list_of_dicts = []
    for char in dict:
        list_of_dicts.append({"char": char, "num": dict[char]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def main():
    doc_to_read = input("Please input the relative path to a document: (e.g. folder/file.txt or ../folder/file.txt): ")
    with open(doc_to_read, encoding='utf-8') as f: # Opens the file and reads in the document contents
        file_contents = f.read() 

        word_list, word_count = count_words(file_contents) # Saves both word and letter count into variables
        letter_count = count_letters(file_contents)
        sorted_letter_dict = dict_to_listdict(letter_count) # Turns the letter dictionary into a sorted list of dictionaries
        word_letter_dict = dict_to_listdict(word_list) # Turns the letter dictionary into a sorted list of dictionaries

        # Prints out the actual report
        
        print()
        print("--- Begin report for number of words and letters ---")
        print()
        print(f"This document has {word_count} words.") # Prints word count
        print()
        for item in sorted_letter_dict: # Prints out the number of alphabetic characters (English)
            if item["char"].isalpha():
                print(f"The {item['char']} character was found {item['num']} times")
        print()
        for item in word_letter_dict: # Prints out the number of different words (English) that are counted more than 10 times
            if item['num'] > 10:
                print(f"The word '{item['char']}' was found {item['num']} times")
        print()
        print("--- End of report ---")

main()