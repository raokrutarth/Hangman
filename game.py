from util import *
import random
#Krutarth Rao
class Game:
    def __init__(self, fileName):
        self.fileName = fileName
        self.secretWord = self.getRandomWordFromFile()
        self.current = '-' * len(self.secretWord)
        self.wrongTrials = 0
 
    # Returns a random word from the file: self.fileName
    def getRandomWordFromFile(self):
    # TODO:
       # Open self.fileName in the read mode
        file = open(self.fileName, 'r')
       # Read the lines from the file

        words_list = file.readlines()
        
        # And return a random line
        rnd_indx = random.randint(0,len(words_list))
        
        return words_list[rnd_indx].strip()
            # Make sure you strip() before you return
 
    # Returns whether all of the word is found by guessing
    def isFinished(self):
        # TODO:
        # Check if any '-' in self.current
        dash_counter = 0
        for a in self.current:
            if a == '-':
                dash_counter +=1
        if dash_counter == 0:
            return True
        else:
            return False
        # Return true if no '-' in self.current
        # Return false if there is at least one '-' in self.current
 
    def update(self, guessedCharacter):
        temp = ''
        isTrueGuess = False
        for i in range(0, len(self.secretWord)):
            if self.secretWord[i] == guessedCharacter:
                temp += self.secretWord[i]
                isTrueGuess = True
            else:
                temp += self.current[i]
 
        self.current = temp
        return isTrueGuess
    def play(self):
        while not self.isFinished():
            Util.clearScreen()
            Util.drawMan(self.wrongTrials)
            print('Current value: ' + self.current)
 
            if self.wrongTrials == 6:
                print('you lost')
                break
 
            guessedCharacter = input('Make a guess: ')
            result = self.update(guessedCharacter)
 
            if result == False:
                self.wrongTrials += 1
 
        if self.isFinished():
            print('you win')
