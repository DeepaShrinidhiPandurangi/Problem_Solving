# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print(wordlist)
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for i,j in enumerate(secretWord):
      if j in lettersGuessed:
        count+=1
    return count == len(secretWord)

      
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s = ''
    for i,j in enumerate(secretWord):
      if j in lettersGuessed:
        s = s + j
      else:
        s = s + '_ '
    return s
    
      

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    s = ''
    for i in string.ascii_lowercase:
      if i not in lettersGuessed:
        s = s+i
    return s
    

def hangman(secretWord):
    lettersGuessed = []
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord), "letters long")
    print("-------------")

    guess = 8
    
    while guess > 0 and guess <= 8 and isWordGuessed(secretWord, lettersGuessed) == False: # or the last parameter "_" in getGuessedWord(secretWord,lettersGuessed):
      print("You have", guess ,"guesses left")
      print("Available Letters:",getAvailableLetters(lettersGuessed))
      x = input("Please guess a letter:").lower()
      if x not in lettersGuessed:
        if x in secretWord:
          lettersGuessed.append(x)
          print("Good guess:",getGuessedWord(secretWord, lettersGuessed))
        else:
          lettersGuessed.append(x)
          guess -= 1
          print("Oops! That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed))
      else:
        print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
      print("-------------")

    if isWordGuessed(secretWord, lettersGuessed) == True:
      print("Congratulations, you won!")
    else:
      print("Sorry, you ran out of guesses. The word was", secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'z' #chooseWord(wordlist)
hangman(secretWord)
