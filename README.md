# Word Count 4.0 README

## Project Overview
The Word Count 4.0 program allows the users to count occurrences of a specific word or phrase within a file or all files in a directory. 

## Significance 
This program is useful for analyzing text files in bulk, helping the user gather insights into how frequently certain words or phrases appear.

## Features
- **Single File or Directory Search**: Users can count word occurrences in one file or scan through all files in a specified directory.
- **Case Sensitivity Option**: The program would count the words in a case-sensitive way, for example, distinguishing between "Hello" and "hello".
- **CSV Output**: The results are appended to a CSV file (`wordcount_results.csv`), storing the word/phrase, its file location, and the count of occurences.

## Program Instructions
### Running the Program Manually
1. Run the program in the terminal:
   ```bash
   python word_count_4.py
2. Enter the following information as prompted:
- **File or Directory Path:** Provide the path of the file or directory you wish to search.
- **Word or Phrase:** Enter the word or phrase you want to count.
- **Case-Sensitivity** Enter "Yes" for case-sensitive counting or "No" to ignore case-sensitivity.

### Running the Program Using Command-Line Arguments
Run the program in terminal with the following command-line arguments for automatted processing:
```bash 
python word_count_4.py <file_or_directory_path> <word_to_count> <case_sensitive>
```

## Output
- The program prints the count to the terminal and appends the result to (`wordcount_results.csv`).

## Why This is Helpful
This README covers how to run the program and explains the difference between running the program by manual input and using command-line arguments. With this explanation, some potential issues that users would have otherwise faced with include:

- Confusion about file vs. directory handling, especially regarding output destinations of the output for the various modes.
- Not understanding the case-sensitivity option or knowing the required format.
- Errors when insufficient command-line arguments are provided, making it unclear how to proceed further.