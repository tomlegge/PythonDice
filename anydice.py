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

# Generate a random number to see if the dice falls off the table

falloff = str(random.randint(1, 10000000))

# take the random number variables and match them to a number animation
print("\nRolling your dice..\n"); sleep(0.2)
print("You catch a glimpse of a:\n"); sleep(0.2)
if falloff ==1:
    print("Your dice fell off the table! Start again")
else:
    if "1" in rolling1: 
        dicenumbers.print_one(); sleep(0.2)
    else:
        if "2" in rolling1:
            dicenumbers.print_two(); sleep(0.2)
        else:
            if "3" in rolling1:
                dicenumbers.print_three(); sleep(0.2)
            else:
                if "4" in rolling1:
                    dicenumbers.print_four(); sleep(0.2)
                else:
                    if "5" in rolling1:
                        dicenumbers.print_five(); sleep(0.2)
                    else:
                        if "6" in rolling1:
                            dicenumbers.print_six(); sleep(0.2)
                        else:
                            print(rolling1); sleep(0.2)
print("\nBut it is still rolling..\n"); sleep(0.2)
print("You think you've seen a..\n"); sleep(0.2)
if "1" in rolling2: 
    dicenumbers.print_one(); sleep(0.2)
else:
    if rolling2 == 2:
        dicenumbers.print_two(); sleep(0.2)
    else:
        if rolling2 ==3:
            dicenumbers.print_three(); sleep(0.2)
        else:
            if rolling2 ==4:
                dicenumbers.print_four(); sleep(0.2)
            else:
                if rolling2 ==5:
                    dicenumbers.print_five(); sleep(0.2)
                else:
                    if rolling2 ==6:
                        dicenumbers.print_six(); sleep(0.2)
                    else:
                        print(rolling2); sleep(0.2)
print("\nBut it's still rolling..\n"); sleep(0.2)
if rolling3 ==1: 
    dicenumbers.print_one(); sleep(0.2)
else:
    if rolling3 ==2:
        dicenumbers.print_two(); sleep(0.2)
    else:
        if rolling3 ==3:
            dicenumbers.print_three(); sleep(0.2)
        else:
            if rolling3 ==4:
                dicenumbers.print_four(); sleep(0.2)
            else:
                if rolling3 ==5:
                    dicenumbers.print_five(); sleep(0.2)
                else:
                    if rolling3 ==6:
                        dicenumbers.print_six(); sleep(0.2)
                    else:
                        print(rolling3); sleep(0.2)
print("\nWhat was that? Surely, its going to stop soon..\n"); sleep(0.2)

print("Aaah, finally - your dice landed on: \n"); sleep(0.2)


if final_string ==1: 
    dicenumbers.print_one(); sleep(0.2)
else:
    if final_string ==2:
        dicenumbers.print_two(); sleep(0.2)
    else:
        if final_string ==3:
            dicenumbers.print_three(); sleep(0.2)
        else:
            if final_string ==4:
                dicenumbers.print_four(); sleep(0.2)
            else:
                if final_string ==5:
                    dicenumbers.print_five(); sleep(0.2)
                else:
                    if final_string ==6:
                        dicenumbers.print_six(); sleep(0.2)
                    else:
                        print(final_string)
        