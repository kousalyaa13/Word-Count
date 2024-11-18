# example using input()

import sys 

# print(sys.argv)
# print(type(sys.argv))
# print(f"Here's the third argument after the script name: {sys.argv[3]}")

#this automates the actions
if len(sys.argv) >= 3:
    #get values from command line
    word_to_repeat = sys.argv[1]
    times_to_repeat = sys.argv[2]
    # terminal command:
    # python input_vs_argv.py "happy halloween" 30

else:
    # get values from user
    word_to_repeat = input("What word or phrase would you like me to repeat?\n")
    times_to_repeat = input("How many times should I repeat it?\n")
    # terminal command:
    # python input_vs_argv.py

# process values
word_to_repeat = word_to_repeat + " "
times_to_repeat = int(times_to_repeat)
string_to_print = word_to_repeat * times_to_repeat

# print results
print(string_to_print)