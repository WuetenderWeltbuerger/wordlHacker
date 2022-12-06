#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "WuetenderWeltbuerger"
__version__ = "0.1.0"
__license__ = "MIT"

import random
from words import words
import string

def getRandomWord(words):
      word = random.choice(words) #randomly selects from the list
      while len(word) != 5: #discards any except 5 letter words
        word = random.choice(words) #re iterates through the list
      #print(word) #for debugging
      return word.upper()

def fiveLetterWords(words):
      listOfWords = [] #initialize new list
      for word in words: #discards any except 5 letter words
        if len(word) != 5:
            continue
        else:
            listOfWords.append(word)
        
      return listOfWords

def letterDistribution():
    #creates a list of the number of times each letter appears
    #in the word list
    listOfWords = fiveLetterWords(words)
    alphabet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for word in listOfWords:
        for letter in word:
            if letter == 'a':
                alphabet[0] += 1
            elif letter == 'b':
                alphabet[1] += 1
            elif letter == 'c':
                alphabet[2] += 1
            elif letter == 'd':
                alphabet[3] += 1
            elif letter == 'e':
                alphabet[4] += 1
            elif letter == 'f':
                alphabet[5] += 1
            elif letter == 'g':
                alphabet[6] += 1
            elif letter == 'h':
                alphabet[7] += 1
            elif letter == 'i':
                alphabet[8] += 1
            elif letter == 'j':
                alphabet[9] += 1
            elif letter == 'k':
                alphabet[10] += 1
            elif letter == 'l':
                alphabet[11] += 1
            elif letter == 'm':
                alphabet[12] += 1
            elif letter == 'n':
                alphabet[13] += 1
            elif letter == 'o':
                alphabet[14] += 1
            elif letter == 'p':
                alphabet[15] += 1
            elif letter == 'q':
                alphabet[16] += 1
            elif letter == 'r':
                alphabet[17] += 1
            elif letter == 's':
                alphabet[18] += 1
            elif letter == 't':
                alphabet[19] += 1
            elif letter == 'u':
                alphabet[20] += 1
            elif letter == 'v':
                alphabet[21] += 1
            elif letter == 'w':
                alphabet[22] += 1
            elif letter == 'x':
                alphabet[23] += 1
            elif letter == 'y':
                alphabet[24] += 1
            elif letter == 'z':
                alphabet[25] += 1
    return alphabet
            
def convert(list):
    return tuple(list) #funciton to convert lists to tuples

def determineStartingWord():    
    
    alphabet = letterDistribution()
    alphabetTuple = convert(alphabet)
    alphabetTuple.index(max(alphabetTuple))
    distributionList = []
    i = 1
    while i < 6:
      x = alphabetTuple.index(max(alphabetTuple))
      alphabet[x] = 0
      alphabetTuple = convert(alphabet)
      distributionList.append(x)
      i += 1
    print(distributionList)
    
    
    

  
  
def main():
    determineStartingWord()
    print()
    



    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()