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
import re

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

def weighDistribution():    
    #creates list with number of occurences in each word
    alphabet = letterDistribution()
    #initialize list as a tuple
    alphabetTuple = convert(alphabet)
    #initialize empty list
    distributionList = []
    i = 1
    while i < 6:
      #get index of highest number of occurences
      x = alphabetTuple.index(max(alphabetTuple))
      #set that index to 0 in the alphabet list to prevent it from being called again
      alphabet[x] = 0
      #replace tuple with updated alphabet
      alphabetTuple = convert(alphabet)
      #add the location of x to the distribution list
      distributionList.append(x)
      i += 1
    return distributionList
    
def determineStartingWord():
    #uses the output of the weightDistribtution function to find the
    #most likely word in the list
    weightOutput = weighDistribution()
    tempList = []
    validWords = fiveLetterWords(words)
    for x in weightOutput:
        if x == 0:
            tempList.append('a')
        if x == 1:
            tempList.append('b')
        if x == 2:
            tempList.append('c')
        if x == 3:
            tempList.append('d')
        if x == 4:
            tempList.append('e')
        if x == 5:
            tempList.append('f')
        if x == 6:
            tempList.append('g')
        if x == 7:
            tempList.append('h')
        if x == 8:
            tempList.append('i')
        if x == 9:
            tempList.append('j')
        if x == 10:
            tempList.append('k')
        if x == 11:
            tempList.append('l')
        if x == 12:
            tempList.append('m')
        if x == 13:
            tempList.append('n')
        if x == 14:
            tempList.append('o')
        if x == 15:
            tempList.append('p')
        if x == 16:
            tempList.append('q')
        if x == 17:
            tempList.append('r')
        if x == 18:
            tempList.append('s')
        if x == 19:
            tempList.append('t')
        if x == 20:
            tempList.append('u')
        if x == 21:
            tempList.append('v')
        if x == 22:
            tempList.append('w')
        if x == 23:
            tempList.append('x')
        if x == 24:
            tempList.append('y')
        if x == 25:
            tempList.append('z')
    
    #assign variables
    letter1 = tempList[0]
    letter2 = tempList[1]
    letter3 = tempList[2]
    letter4 = tempList[3]
    letter5 = tempList[4]
    
    #create empty strings
    possible1 = []
    possible2 = []
    possible3 = []
    possible4 = []
    possible5 = []
     
    #itterate through valid word list and populate 4 lists
    #with possible answers to the problem
    for word in validWords:
        for letter in word:
            if letter1 == letter:
                possible1.append(word)
                continue
            else:
                continue
             
               
    for word in possible1:
        for letter in word:
            if letter2 == letter:
                possible2.append(word)
                continue
            else:
                continue

    for word in possible2:
        for letter in word:
            if letter3 == letter:
                possible3.append(word)
                continue
            else:
                continue
    
    for word in possible3:
        for letter in word:
            if letter4 == letter:
                possible4.append(word)
                continue
            else:
                continue
    
    for word in possible4:
        for letter in word:
            if letter5 == letter:
                possible5.append(word)
                continue
            else:
                continue
    
    return possible5
    #uncomment the following to see how the code works
    #or to debug the function
    
    #print(letter1)
    #print(possible1)
    #print(possible2)
    #print(possible3)
    #print(letter4)
    #print(possible4)
    #print(letter5)
    #print(possible5)

def isUpperCase(letter):
    if letter == "A":
        return True
    if letter == "B":
        return True
    if letter == "C":
        return True
    if letter == "D":
        return True
    if letter == "E":
        return True
    if letter == "F":
        return True
    if letter == "G":
        return True
    if letter == "H":
        return True
    if letter == "I":
        return True
    if letter == "J":
        return True
    if letter == "K":
        return True
    if letter == "L":
        return True
    if letter == "M":
        return True
    if letter == "N":
        return True
    if letter == "O":
        return True
    if letter == "P":
        return True
    if letter == "Q":
        return True
    if letter == "R":
        return True
    if letter == "S":
        return True
    if letter == "T":
        return True
    if letter == "U":
        return True
    if letter == "V":
        return True
    if letter == "W":
        return True
    if letter == "X":
        return True
    if letter == "Y":
        return True
    if letter == "Z":
        return True
    else:
        return False

def letterChecker(userInput):
    validWords = fiveLetterWords(words) #get valid 5 letter words from external list
    possible1 = [] #initialize empty list for words with matching positions
    possible2 = [] #intiialize empty list for words without matching positions
    for letter in userInput:
        if letter == "-":
            #if the
            continue
        if letter is isUpperCase(letter):
            for word in validWords:
               
            
             continue   
            
            
        if letter is not isUpperCase(letter):    
            for word in validWords:
                if word == letter:
                    possible2.append()
                    continue
                    
    
    return
    

def comparePlayed(played, firstResult):
    correctPosition = []
    i = 0 #counter
    while i < 5:
        if played[i] == firstResult[i]:
            correctPosition[i] = played[i]
            i += 1
            continue
        else:
            correctPosition[i] = "-"
            i += 1
            continue
        
    print(correctPosition)
    return correctPosition
            
  
  
def main():
    startingWord = determineStartingWord()
    print("Welcome to WordlHacker, I am here to help!")
    selection1 = input("Please select from the following:\n[a] new game\n[b] help with an existing game\n")
    if selection1 == "a":
        print("Try starting with one of these words: "+str(startingWord))
    print("""
Please enter the word that you played
each lowercase letter must be seperated by a space:
              """)
    wordPlayed = input("")
    parsePlayed = wordPlayed.split(" ")
    print("""
Please enter the response from Wordl in the following format:
if the letter is in the right position type it in upper case
if it is a valid letter but in the wrong position type it in lower case
if it is not a valid letter please enter a dash
all characters must be seperated by a space
example: S a t - -              
              """)
    firstResult = input("")
    parseFirst = firstResult.split(" ")
    firstLower = firstResult.lower()
    parseFirstLower = firstLower.split(" ")
    comparePlayed(parsePlayed, parseFirstLower)
    letterChecker(parseFirst)



    print(parseFirst)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()