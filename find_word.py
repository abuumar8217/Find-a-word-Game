#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 16:28:14 2021

@author: abuumar
"""
import random
from uzwords import words

def get_word():
    # validletters = 'abcdefghijklmnopqrstuvwxyz'
    validletters = 'йцукенгшўзхъфқвапролджэячсмитьбюғҳё'
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    # print(word)
    guessmade = ''
    while len(word) > 0:
        main = ""
                                            #word is random chosen word out of list needs to be guessed
        for letter in word:
            #print("<letter>" + letter)      #letter is each character of a word to be guessed
            if letter in guessmade:         #guessmade is set of guessed characters
                main += letter.upper()        #guess is entered/guessed character
                                            # main is each letter of guessed word
            else:
                main += "-" + " "
        if main.lower() == word:
            #print("<main>" + main)
            print(f"You did it! You found it in {len(guessmade)} tries")
            print(f"word is {word}")
            break

        print("Guess the word : " , main)
        guess = input(">>>")

        if guess in validletters:
            guessmade = guessmade + guess
            print("<guessmade>" + guessmade)
        else:
            print("Enter valid character")
            guess = input()    
            
get_word()
