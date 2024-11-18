import os
import sys
#import the helper functions
import word_count_helpers as helpers

#check if the command-line arguments are provided
if len(sys.argv) <= 3:
    #automate the inputs
    chosen_path = input("Enter a valid file or directory path: ")
    chosen_word = input("Which word would you like to be counted? ")
    ask_case = input("Do you want this word to be case-sensitive (Yes/No)? ")
    case_sensitive = ask_case.strip().lower() == "yes"

else:
    #get the path and word from the command-line arguments
    chosen_path = sys.argv[1]
    chosen_word = sys.argv[2]

    #check for case-sensitivity and default to case-insensitive
    case_sensitive = False
    if len(sys.argv) > 3:
        case_sensitive = sys.argv[3].lower() == "yes"

#change the current working directory to the assignment folder in Unit 4
os.chdir(r'C:\Users\kousa\Documents\INST126\Unit 7\Text_Files')
#print("This is the current working directory: ", os.getcwd())
#print("This is the list of contents in the directory: ", os.listdir())

#validate the provided path
if not os.path.exists(chosen_path):
    print(f"The path {chosen_path} is not found. Please try again.")
    sys.exit(1)

#check if there are more than one spaces
space_counter = chosen_word.count(" ")
#if there is more than one space, quit the program with an informative message
if (space_counter > 1):
    print("The word/phrase cannot be longer than two words")
    sys.exit(1)

#initialize total count
total_count = 0

#open the results CSV file in the append mode
with open("wordcount_results.csv", "a") as csv_file:
   
   #calculate the count of how many times a word repeats in a text file
    if os.path.isfile(chosen_path):
        #process a single file
        word_count = helpers.get_word_count_in_file(chosen_path, chosen_word, case_sensitive)
        #the output should be printed to the terminal
        print(f"The word '{chosen_word}' was found {word_count} time(s) in this file: {chosen_path}")
        #need to get the directory name/ cwd
        csv_file.write(f"{chosen_word},{os.getcwd()},{os.path.basename(chosen_path)},{word_count}\n")
        total_count = word_count

    # If the user selected a directory
    elif os.path.isdir(chosen_path):
        total_count = helpers.process_directory(chosen_path, chosen_word, case_sensitive)
        print(f"The word '{chosen_word}' was found {total_count} time(s) in the directory: {chosen_path}")
        with open("wordcount_results.txt", "w") as output_file:
            output_file.write(f"The word '{chosen_word}' was found {total_count} time(s) in the directory: {chosen_path}")