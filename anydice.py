# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:50:00 2020

@author: Tom Legge
"""

# Import libraries needed for this programme
import random, dicenumbers
from time import sleep

    
# Getting the user input
n = input('\nHow many sides to you want on your dice?: ')

# Convert user input into an integer
num = int(n)

# Generate a series of random numbers using the 'num' as the higheset possible number and convert each one to a string

rolling1 = str(random.randint(1, num))

rolling2 = str(random.randint(1, num))

rolling3 = str(random.randint(1, num))

final = random.randint(1, num)
final_string = str(final)



# take the random number variables and match them to a number animation
print("\nRolling your dice..\n"); sleep(2)
print("You catch a glimpse of a:\n"); sleep(2)
if "1" in rolling1: 
    dicenumbers.print_one(); sleep(2)
else:
    if "2" in rolling1:
        dicenumbers.print_two(); sleep(2)
    else:
        if "3" in rolling1:
            dicenumbers.print_three(); sleep(2)
        else:
            if "4" in rolling1:
                dicenumbers.print_four(); sleep(2)
            else:
                if "5" in rolling1:
                    dicenumbers.print_five(); sleep(2)
                else:
                    if "6" in rolling1:
                        dicenumbers.print_six(); sleep(2)
                    else:
                        print(rolling1); sleep(2)
print("\nBut it is still rolling..\n"); sleep(2)
print("You think you've seen a..\n"); sleep(2)
if "1" in rolling2: 
    dicenumbers.print_one(); sleep(2)
else:
    if "2" in rolling2:
        dicenumbers.print_two(); sleep(2)
    else:
        if "3" in rolling2:
            dicenumbers.print_three(); sleep(2)
        else:
            if "4" in rolling2:
                dicenumbers.print_four(); sleep(2)
            else:
                if "5" in rolling2:
                    dicenumbers.print_five(); sleep(2)
                else:
                    if "6" in rolling2:
                        dicenumbers.print_six(); sleep(2)
                    else:
                        print(rolling2); sleep(2)
print("\nBut it's still rolling..\n"); sleep(2)
if "1" in rolling3: 
    dicenumbers.print_one(); sleep(2)
else:
    if "2" in rolling3:
        dicenumbers.print_two(); sleep(2)
    else:
        if "3" in rolling3:
            dicenumbers.print_three(); sleep(2)
        else:
            if "4" in rolling3:
                dicenumbers.print_four(); sleep(2)
            else:
                if "5" in rolling3:
                    dicenumbers.print_five(); sleep(2)
                else:
                    if "6" in rolling3:
                        dicenumbers.print_six(); sleep(2)
                    else:
                        print(rolling3); sleep(2)
print("\nWhat was that? Surely, its going to stop soon..\n"); sleep(2)

print("Aaah, finally - your dice landed on: \n"); sleep(2)


if "1" in final_string: 
    dicenumbers.print_one(); sleep(2)
else:
    if "2" in final_string:
        dicenumbers.print_two(); sleep(2)
    else:
        if "3" in final_string:
            dicenumbers.print_three(); sleep(2)
        else:
            if "4" in final_string:
                dicenumbers.print_four(); sleep(2)
            else:
                if "5" in final_string:
                    dicenumbers.print_five(); sleep(2)
                else:
                    if "6" in final_string:
                        dicenumbers.print_six(); sleep(2)
                    else:
                        print(final_string)
        