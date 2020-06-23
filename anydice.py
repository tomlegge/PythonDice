# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:50:00 2020

@author: Tom Legge
"""

# Import libraries needed for this programme
import random, dicenumbers
from time import sleep

# Set the time delay between each message
delay = 0.7
# Getting the user input and converting it to an integer
n = int(input('\nHow many sides to you want on your dice?: '))

# Does the user have a rolling tray? This reduces the probability of the dice rolling off the table
tray = input('\nAre you going to use a dice tray? Answer Yes or No: ')
if tray == 'Yes':
    prob = 1000000
else:
    prob = 1

# Generate some random numbers, taking the user input as the maximum number.
rolling1 = int(random.randint(1, n))
rolling2 = int(random.randint(1, n))
rolling3 = int(random.randint(1, n))
final_string = int(random.randint(1, n))

# Generate a random number to see if the dice falls off the table. Highest the second number, lower the probability of the dice falling off the table
falloff = int(random.randint(1, prob))

# Setting a boolen variable to equal False - if the dice falls off the table, this is changed to True
felloff  = bool(False)

# take the random number variables and match them to a number animation
print("\nYou roll your dice..\n"); sleep(delay)

if falloff ==1:
    print("Your dice fell off the table! Fucks sake you amateur"); sleep(delay*2)
    felloff = True
else:
    print("You catch a glimpse of a:\n"); sleep(delay*2)
    if rolling1 ==1: 
        dicenumbers.print_one(); sleep(delay)
    else:
        if rolling1 ==2:
            dicenumbers.print_two(); sleep(delay)
        else:
            if rolling1 ==3:
                dicenumbers.print_three(); sleep(delay)
            else:
                if rolling1 ==4:
                    dicenumbers.print_four(); sleep(delay)
                else:
                    if rolling1 ==5:
                        dicenumbers.print_five(); sleep(delay)
                    else:
                        if rolling1 ==6:
                            dicenumbers.print_six(); sleep(delay)
                        else:
                            print(rolling1); sleep(delay)

if felloff is True:
    print("\nYou should really pick up your dice, you clumsy donkey cock!"); sleep(delay*2)
else:
    print("\nBut it is still rolling..\n"); sleep(delay)
    print("You think you've seen a..\n"); sleep(delay*2)
    if rolling2 == 1:
        dicenumbers.print_one(); sleep(delay)
    else:
        if rolling2 == 2:
            dicenumbers.print_two(); sleep(delay)
        else:
            if rolling2 ==3:
                dicenumbers.print_three(); sleep(delay)
            else:
                if rolling2 ==4:
                    dicenumbers.print_four(); sleep(delay)
                else:
                    if rolling2 ==5:
                        dicenumbers.print_five(); sleep(delay)
                    else:
                        if rolling2 ==6:
                            dicenumbers.print_six(); sleep(delay)
                        else:
                            print(rolling2); sleep(delay)

if felloff is True:
    print("You make me sick! Go on, get out of my sight!"); sleep(delay*6)
else:
    print("It's still rolling???\n"); sleep(delay*2)
    if rolling3 ==1: 
        dicenumbers.print_one(); sleep(delay)
    else:
        if rolling3 ==2:
            dicenumbers.print_two(); sleep(delay)
        else:
            if rolling3 ==3:
                dicenumbers.print_three(); sleep(delay)
            else:
                if rolling3 ==4:
                    dicenumbers.print_four(); sleep(delay)
                else:
                    if rolling3 ==5:
                        dicenumbers.print_five(); sleep(delay)
                    else:
                        if rolling3 ==6:
                            dicenumbers.print_six(); sleep(delay)
                        else:
                            print(rolling3); sleep(delay)


if felloff is True:
    print("\nTwat"); sleep(delay*2)
else:
    print("\nWhat was that? Surely, its going to stop soon..\n"); sleep(delay)
    print("Aaah, finally - your dice landed on: \n"); sleep(delay*2)
    if final_string ==1: 
        dicenumbers.print_one(); sleep(delay)
    else:
        if final_string ==2:
            dicenumbers.print_two(); sleep(delay)
        else:
            if final_string ==3:
                dicenumbers.print_three(); sleep(delay)
            else:
                if final_string ==4:
                    dicenumbers.print_four(); sleep(delay)
                else:
                    if final_string ==5:
                        dicenumbers.print_five(); sleep(delay)
                    else:
                        if final_string ==6:
                            dicenumbers.print_six(); sleep(delay)
                        else:
                            print(final_string)
        