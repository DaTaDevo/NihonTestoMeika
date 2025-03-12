#
# [] create answer reveal after test for quicker check
import os
import random

clear = lambda : os.system("clear")

# DEBUG: bool = True
DEBUG: bool = False

list = []
#copying data from file to local list
with open("file.txt", "r") as file:
    for elmt in file:
        list.append(elmt.strip()) 
if DEBUG:
    print("[[Length of the list is ", len(list))
numStudyWords: int = int(input("How many words do I want to study?(1-" + str(len(list)) + "): "))
# print("The type of variable $partition is ", type(partition))
limit = numStudyWords
# limit = 0
if DEBUG:
    print("[[The limit for the for loop is ", limit)

print("Let's print all possible words for the test :) ")
for i in range(limit):
    if DEBUG:
        print("[[ i = ", i)
    print("Word #", i+1, list[i] )
if DEBUG:
    print ("[[Now we loop.")
word_num = limit + 1
num_list = [word_num]    
input("The test is ready! Press 'Enter' to start the test!")
clear()

for i in range(limit):
    if DEBUG:
        print("i = ", i)
        print("[[The $word_num before cycle is ", word_num)
        print("[[The check if word is in the list is ",word_num in num_list)
    while word_num in num_list:
        if DEBUG:
            print ("[[Our list is looking like this ", num_list)
        word_num = random.randint(0, limit-1)
        if DEBUG:
            print("[[generated number is ", word_num)
            input("[[While Cycle ended Press anything to continue...");
    num_list.append(word_num)
    if DEBUG:
        print ("[[Now our list is looking like this ", num_list)
        print("[[Our word number is ", word_num)
        print("[[The word under the word number is ", list[word_num])
    # list[word_num]
        input("[[For Cycle ended Press anything to continue...");
    if not DEBUG:
        print("The word is ", list[word_num])
        input("Press to see next word...")
        clear()
print("Congratuations! The test is over!!! ^-^")
# print("Element of the list look like this: \n", list)
