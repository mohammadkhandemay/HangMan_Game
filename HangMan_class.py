# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 09:57:36 2024

@author: mohammad
"""

import string
import random
word_list=['red','yellow','blue','black','pink',
           'brown','white','green','orange','gray']

class HangManGame:
    player_list=list()
    def __init__(self):
        self.name=input("Please Enter Your Name:")
        self.__rand_word=random.choice(word_list)
        self.__win_state=False
        self.__guess_left=len(self.__rand_word)
        self.guessed_letters=[]
        
        self.player_list.append(self)
    def genrate_hints(self,guessed_letters):
        hints=list()
        alphabet=string.ascii_lowercase
        remaining_rand_word=[i for i in [*self.__rand_word] if i not in guessed_letters]
        remaining_alphabet=[i for i in [*alphabet] if i not in guessed_letters]
        mis_hint=[i for i in remaining_alphabet if i not in remaining_rand_word]
        if len(remaining_rand_word)==1:
            hints.extend(random.sample(remaining_rand_word,k=1))
            hints.extend(random.sample(mis_hint,k=4,))
        else:
            hints.extend(random.sample(remaining_rand_word,k=2))
            hints.extend(random.sample(mis_hint,k=3,))
        random.shuffle(hints) 
        return hints
    def minus_guess_left(self):
        self.__guess_left-=1
        print(f'{self.guess_left} guesses left')
    def has_guess_left(self):
        if self.__guess_left>0:
            return True
        else:
            return False
    def has_won(self):
         return self.__win_state
    @classmethod
    def game_has_winner(cls):
        if any(player.has_won() is True for player in cls.player_list):
            return True
        return False
    def uncoverd(self):
        word_uncoverd=list()
        for j in self.__rand_word:
            if j in self.guessed_letters:
                word_uncoverd.append(j)
            else:
                word_uncoverd.append('*')
        return word_uncoverd
    def check_answer(self,guess):
        self.guessed_letters.append(guess)
        if guess in self.__rand_word:
            print(f'congrats {self.name} right guess')
        else:
            print('Wrong guess')
            self.__guess_left-=1
        if [i for i in [*self.__rand_word] if i not in self.guessed_letters]==[]:
            print(f'congratulation {self.name} you have won')
            self.__win_state=True
class GameController:
    def __init__(self):
        
        while True:
            
            for player in HangManGame.player_list:
                if not player.has_guess_left():
                    print(f'Game Over {player.name}!!! You are out of guesses')
                if not player.has_won() and player.has_guess_left():
                   print('\n-------------')
                   print('guess the word:%s' %player.uncoverd())
                   print('hints:%s' %player.genrate_hints(player.guessed_letters))
                   guess=input(f'{player.name} enter your guess: ')
                   player.check_answer(guess)
            
            if HangManGame.game_has_winner():
                break
if __name__=="__main__":
    while True:
        order=input("what do you want to do \norder:")
        if order=="add":
            HangManGame()
        elif order=="start":
            GameController()
        elif order=="exit":
            break
