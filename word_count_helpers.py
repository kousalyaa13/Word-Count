#contains all the helper functions for word_count_4

import os

#function to ask the user for a valid file or directory path
def get_valid_path():
    """
    Asks the user to input a valid file or directory path.
    The function will ask the user repeatedly until a valid path is provided.
    """
    while True:
        #ask the user to enter a path
        chosen_path = input("Enter a valid file or directory path here: ")
        
        #check if the entered path exists
        if os.path.exists(chosen_path):
            #exit the loop because a valid path is given
            return chosen_path
        print(f"The path {chosen_path} is not found. Please try again.")

#function to count occurrences of a word in a file
def get_word_count_in_file(file_path, chosen_word, case_sensitive):
    "Counts the occurrences of a specific word or phrase in the given file."
    
    #open the specified file in read mode
    try:
        with open(file_path, "r") as file:
            content = file.read()
    #if file is not found, return appropriate error
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0
    
    #if not case-sensitive, convert both content and word to lowercase
    if not case_sensitive:
        return content.lower().count(chosen_word.lower())
    return content.count(chosen_word)

#function to process all files in a directory and count the word occurrences
def process_directory(directory_path, chosen_word, case_sensitive):
    "Processes all the text files in a directory and counts the occurrences of a specific word in each file."
    
    #initialize total count
    total_count = 0

    #iterate over all items in the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        
        #check if the item is a file
        if os.path.isfile(item_path):
            #count the occurrences in the current file
            word_count = get_word_count_in_file(item_path, chosen_word, case_sensitive)
            print(f"The word '{chosen_word}' was found {word_count} time(s) in: {item_path}")
            
            #add the word count from the current file to the total count
            total_count += word_count
    return total_count