"""
A file containing the constants needed to play a game of Hangman.

The text file containing the list of words was taken from Parity Technologies
on Github. You can find the file here at this link:
https://github.com/paritytech/wordlist/blob/master/res/wordlist.txt

Author: Will Xiao
Date: Jan 4, 2019
"""
import os
os.chdir('hangman') #so we can be in the right directory to read the text file

NUM_LIVES = 5 #number of incorrect guesses before loss

##GENERATING WORD LIST##
file = open('wordlist.txt')
contents = file.read()

#final word list
WORD_LIST = contents.split('\n')
