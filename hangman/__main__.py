"""
The main method that runs the game of Hangman.

This Hangman game is run in the console/command shell.

Author: Will Xiao
Date: Jan 4, 2019
"""
import hangman

def prompt_user_play():
    """
    Returns: True if the player wants to play another game of Hangman,
    False otherwise.
    """
    inp = ''
    while not inp in ['y', 'n']: #invalid or valid input
        inp = input("Play again? Please enter either 'Y' or 'N'. ").lower()
    return inp == 'y' 


if __name__ == '__main__':
    play_again = True
    while play_again:
        hangman.Hangman().play()
        play_again = prompt_user_play()
