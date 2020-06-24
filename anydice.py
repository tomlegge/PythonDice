# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:50:00 2020

@author: Tom Legge
"""
# Sound credits
## This program uses sound from https://freesound.org/people/LunarThePunar/sounds/322030/ by user LunarThePunar under a creative commons licence &
## This program uses sound from https://freesound.org/people/dylanperitz/sounds/444186/ by the user dylanperitz

# Import libraries needed for this program
import random
## dicenumbers is used to generate the 'images' of the dice
import dicenumbers
from time import sleep
from playsound import playsound

# Set the time delay between each message, in seconds
delay = 0.78

# most of the code is inside the function 'start' so that it can be re-run without having to restart the program
def start():
    # Asking the player how many sides they want on their dice and converting it to an integer
    n = int(input('\nHow many sides to you want on your dice?: '))
    
    # Does the user have a rolling tray? This reduces the probability of the dice rolling off the table. The variable 'prop' us used later as input in a random number generator
    tray = input('\nAre you going to use a dice tray? Answer Y or N: ')
    if tray == 'Y':
        prob = 1000000
    else:
        prob = 10
    
    # Generate some random numbers, taking the player input 'n' as the maximum possible random number.
    rolling1 = int(random.randint(1, n))
    rolling2 = int(random.randint(1, n))
    rolling3 = int(random.randint(1, n))
    final_number = int(random.randint(1, n))
    
    # Generate a random number to see if the dice falls off the table. The variable 'prob' is used for the highest possible number
    falloff = int(random.randint(1, prob))
    
    # Setting a boolen variable to equal False - if the dice falls off the table, this is changed to True
    felloff  = bool(False)
    
    # Play some dramatic music once the dice starts rolling and a sound effect of a dice being shaken and rolled. Allow these to play simultaneously
    playsound('322030__lunarthepunar__tension-building-intro.wav', block = False)
    playsound('444186__dylanperitz__shaking-and-rolling-dice.wav', block = False)
    
    # take the random number variables and match them to a number animation - this shows the progress of the dice as it rolls across the table - or in some cases, falls off
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
                                if rolling1 ==7:
                                    dicenumbers.print_seven(); sleep(delay)        
                                else:
                                    if rolling1 ==8:
                                        dicenumbers.print_eight(); sleep(delay)
                                    else:
                                        if rolling1 ==9:
                                            dicenumbers.print_nine(); sleep(delay)
                                        else:
                                            print(rolling1); sleep(delay)
    
    if felloff is True:
        print("\nYou should really pick up your dice, you clumsy donkey cock!"); sleep(delay*2)
    else:
        print("\nBut it is still rolling..\n"); sleep(delay)
        print("\nYou think you've seen a..\n"); sleep(delay*2)
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
                                if rolling2 ==7:
                                    dicenumbers.print_seven(); sleep(delay)        
                                else:
                                    if rolling2 ==8:
                                        dicenumbers.print_eight(); sleep(delay)
                                    else:
                                        if rolling2 ==9:
                                            dicenumbers.print_nine(); sleep(delay)
                                        else:
                                            print(rolling2); sleep(delay)
    
    if felloff is True:
        print("You make me sick! Go on, get out of my sight!"); sleep(delay*6)
    else:
        print("\nYou've seen a flash of a ...?\n"); sleep(delay*2)
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
                                if rolling3 ==7:
                                    dicenumbers.print_seven(); sleep(delay)        
                                else:
                                    if rolling3 ==8:
                                        dicenumbers.print_eight(); sleep(delay)
                                    else:
                                        if rolling3 ==9:
                                            dicenumbers.print_nine(); sleep(delay)
                                        else:
                                            print(rolling3); sleep(delay)
    
    
    if felloff is True:
        print("\nTwat"); sleep(delay*2)
    else:
        print("\nBut it is still rolling..\n"); sleep(delay)
        print("\nAaah, finally -it has stopped and your dice landed on: \n"); sleep(delay*2)
        if final_number ==1: 
            dicenumbers.print_one(); sleep(delay)
        else:
            if final_number ==2:
                dicenumbers.print_two(); sleep(delay)
            else:
                if final_number ==3:
                    dicenumbers.print_three(); sleep(delay)
                else:
                    if final_number ==4:
                        dicenumbers.print_four(); sleep(delay)
                    else:
                        if final_number ==5:
                            dicenumbers.print_five(); sleep(delay)
                        else:
                            if final_number ==6:
                                dicenumbers.print_six(); sleep(delay)
                            else:
                                if final_number ==7:
                                    dicenumbers.print_seven(); sleep(delay)        
                                else:
                                    if final_number ==8:
                                        dicenumbers.print_eight(); sleep(delay)
                                    else:
                                        if final_number ==9:
                                            dicenumbers.print_nine(); sleep(delay)
                                        else:
                                            print(final_number); sleep(delay)


restart = bool(True)

while restart is True:
    start()
        