"""
A module to represent the Hangman game.

This file contains all the functions required to run a game of Hangman.
Calling the play() method will initiate a game of Hangman.

Author: Will Xiao
Date: Jan 4, 2019
"""
from consts import *
import random

class Hangman(object):
    """
    An instance represents a game of Hangman, with a certain guessing word,
    number of guesses left, etc.

    Instance attributes:
    _word: the word to guess [String, empty if word has not been chosen yet]
    _guesses: the number of incorrect guesses left before the player loses [int]
    _hidden_word: the word, but with the unguessed letters hidden as underscores [str]
    _used: the letters that have been guessed already [list of letters, no duplicates]
    """

    def __init__(self):
        """
        Initializes a game of Hangman and sets all the relevant attributes.
        """
        self._guesses = NUM_LIVES
        self._word = ''
        self._hidden_word = ''
        self._used = []


    def play(self):
        """
        This method initiates a console-run game of Hangman.
        """
        print('Welcome to Hangman.')
        word_length = self._pick_length()
        self._word = self._generate_random_word(word_length)
        self._generate_hidden_word()

        while self._game_not_done():
            print('Current status: ' + self._hidden_word)
            letter = self._prompt_user_guess()
            self._update_word(letter)
            #continue guessing and playing

        if self._guesses == 0:
            self._player_lost()
        else:
            self._player_won()

    def _pick_length(self):
        """
        Promps the user to put in a number between 3 and 9 to use as the length
        of the word to be generated. If the user puts in an invalid input, the
        method will keep prompting the user until a correct one is provided.
        """
        print('What difficulty would you like to play at?')
        print('Pick a number between 3 and 9. A word of that length will be generated.')

        word_len = -1
        while word_len == -1:
            x = input('Enter a number: ')
            if not self._is_int(x):
                print('You need to provide an int.')
            elif not int(x) in range(3,10):
                print('The number must be between 3 and 9.')
            else:
                print('You entered: ' + x + '.')
                word_len = int(x)
        return word_len

    def _is_int(self, val):
        """
        Returns: True if val is a string corresponding to an int, False otherwise.

        Parameter val: the value to check
        Precondition: val is a string
        """
        try:
            int(val)
            return True
        except:
            return False

    def _generate_random_word(self, length):
        """
        Generates a random word of length length.

        Parameter length: the length of the word to generate.
        Precondition: length is an int between 3 and 9.
        """
        filtered_list = tuple(filter(lambda v : len(v) == length, WORD_LIST))
        return random.choice(filtered_list)

    def _generate_hidden_word(self):
        """
        Generates the hidden word based on the word.

        Precondition: the _word attribute must have already been generated.
        """
        word = '_ ' * len(self._word)
        self._hidden_word = word[:-1]

    def _word_not_guessed(self):
        """
        Returns: True if the word has not completely been uncovered, False otherwise.
        """
        return '_' in self._hidden_word

    def _game_not_done(self):
        """
        Returns: True if the hangman game has not finished, False otherwise.

        The game has not finished if the player still has lives and has not
        guessed the entire word.
        """
        return self._guesses != 0 and self._word_not_guessed()

    def _prompt_user_guess(self):
        """
        Returns: the letter the player guesses.

        This function also adds the guessed letter to the list of letters the
        player has guessed already.

        If the user does not input a valid letter, the console will keep
        prompting them until they do.
        """
        letter = ''
        judged_input = self._judge_input(letter)
        while judged_input != (True, True, True):
            inp = input('Enter a letter: ')
            judged_input = self._judge_input(inp)
            if judged_input[0] == False:
                print('You need to input 1 character.')
            elif judged_input[1] == False:
                print('You need to input an alphabetical character.')
            elif judged_input[2] == False:
                print('You need to guess a new letter.')
            else:
                print('You guessed: ' + inp)
                letter = inp
                self._used.append(letter)
        return letter

    def _judge_input(self, letter):
        """
        Returns: A tuple (bool, bool, bool) corresponding to whether
        letter is a valid input (it has the following properties):
        (one character long, is alphabetical, not been guessed already)

        Parameter letter: the input to check
        Precondition: letter is a str
        """
        return (len(letter) == 1, letter.isalpha(), not letter in self._used)

    def _update_word(self, letter):
        """
        Updates the hidden word based on letter.

        If letter is in the hidden word and has not been uncovered yet,
        it will be uncovered.

        If it is not, then a life will be deducted.
        """
        if letter in self._word:
            #uncover the hidden letter from the word
            for i in range(len(self._word)):
                if self._word[i] == letter:
                    wd = self._hidden_word[:2*i] + letter + self._hidden_word[(2*i)+1:]
                    self._hidden_word = wd
            print('You correctly guessed a letter!')

        else: #not in word, deduct life
            self._guesses -= 1
            print('That letter was not in the hidden word.')
            print('You have ' + str(self._guesses) + ' lives left.')

    def _player_lost(self):
        """
        Displays the losing message.
        """
        print('You ran out of guesses!')
        print('The word was: ' + str(self._word) + '.')
        print('Good game.')

    def _player_won(self):
        """
        Displays the winning message.
        """
        print('You guessed the word!')
        print('The word was: ' + str(self._word) + '.')
        print('Congratulations.')
