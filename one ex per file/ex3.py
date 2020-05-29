# part 3
# Task: 
# - break s into a list of words (i.e. now separated by space)
# - print out the word list (with a loop) so that every 2. word is in full uppercase.
# - optionally remove all periods and commas
# result:
# Python
# IS
# an
# INTERPRETED
# high-level
# GENERAL-PURPOSE
# programming
# LANGUAGE
print("start of part 3") # set breakpoint here
# your code here
s = "Python is an interpreted, high-level, general-purpose programming language."
word_list = s.split() # split the string in an list of word elements
upper_case = False  
for word in word_list:
    # replace characters with empty element
    word = word.replace('.', '')
    word = word.replace(',', '')
    if upper_case == True:
        print(word.upper())
        upper_case = False
    else:
        print(word)
        upper_case = True

print("end of 3") # set breakpoint here 
'''



























# solution 3
# version 1 - using 1/-1
s = "Python is an interpreted, high-level, general-purpose programming language."
words = s.split()
make_upper = -1  # we start with 1 for normal print-out, then flip -1 for uppercase, then back, etc.
for w in words:
    w = w.replace('.', '') # replace . with empty list
    w = w.replace(',', '') # replace , with empty list
    if make_upper == 1:
        print(w.upper())
    else:
        print(w)
    make_upper *= -1 # flip from 1 to -1 or vice versa

# version 2 - using 
s = "Python is an interpreted, high-level, general-purpose programming language."
words = s.split()
make_upper = False  # we start with False for normal print-out, then flip to True for uppercase, then back, etc.
for w in words:
    w = w.replace('.', '') # replace . with empty list
    w = w.replace(',', '') # replace , with empty list
    if make_upper == True:
        print(w.upper())
        make_upper = False # it's currently True, so set to False
    else:
        print(w)
        make_upper = True # it must currently be False, so set to True
'''