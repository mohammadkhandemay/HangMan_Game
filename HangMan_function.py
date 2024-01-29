# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:17:41 2023

@author: mohammad
"""

import string
import random
word_list=['red','yellow','blue','black','pink',
           'brown','white','green','orange','gray']
rand_word=random.choice(word_list)
guess_left=len(rand_word)
guessed_letters=list()
def genrate_hints(rand_word,guessed_letters):
    hints=list()
    alphabet=string.ascii_lowercase
    remaining_rand_word=[i for i in [*rand_word] if i not in guessed_letters]
    remaining_alphabet=[i for i in [*alphabet] if i not in guessed_letters]
    mis_hint=[i for i in remaining_alphabet if i not in remaining_rand_word]
    hints.extend(random.choices(remaining_rand_word,k=2))
    hints.extend(random.choices(mis_hint,k=3,))
    random.shuffle(hints) 
    return hints    

player_name=input('please enter your name:')
while True:
    word_uncoverd=list()
    if guess_left==0:
        print('Game Over!!! the right answer was %s'%(rand_word))
        break
    for j in rand_word:
        if j in guessed_letters:
            word_uncoverd.append(j)
        else:
            word_uncoverd.append('*')
    if not '*' in word_uncoverd:
        print('congratulation you have won')
        break
    #hints
    hints=genrate_hints(rand_word, guessed_letters)
    print('you have guessed : %s'%(word_uncoverd))
    print('guess_left = %s'%(guess_left))
    print('hints:%s'%(hints))
    guess=input('please enter your guess:')
    guessed_letters.append(guess)
    if guess in rand_word:
        print('congrats right guess')
    else:
        print('Wrong guess')
        guess_left-=1
        