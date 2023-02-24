import random
from colorama import Fore, Back, Style

wordList = []
with open('words.txt', 'r') as f:
    for line in f.readlines():
        words = line.strip().split(',')
        wordList.append(words[0])

print(Fore.GREEN+"\nWORDLE\n"+Fore.RESET)
print("Guess the WORDLE in six tries.")
print("Each guess must be a valid five-letter word. Hit the enter button to submit.")
print("After each guess, the color of the letter will change to show how close your guess was to the word.\n")
print(Fore.GREEN+"Green means that you guessed the correct letter and correct spot."+Fore.RESET)
print(Fore.YELLOW+"Yellow means that you guessed the correct letter but wrong spot."+Fore.RESET)
print(Fore.RED+"Red means that the letter is not in the word.\n"+Fore.RESET)

w = random.choice(wordList)
guesses = 6
todaysWord = []
usedLetters = []

print("Enter a 5 letter word.")
print("Guesses: 6\n")
for i in w:
    todaysWord.append(i)

inputw = input()
inputWord = []
for i in inputw:
    inputWord.append(i)

def checkWord(inputWord,todaysWord):
    for index in range(5):
        if inputWord[index] == todaysWord[index]:
            print(Fore.GREEN+inputWord[index]+Fore.RESET,end="")
        elif (inputWord[index] in todaysWord) and (inputWord[index] != todaysWord[index]):
            print(Fore.YELLOW+inputWord[index]+Fore.RESET,end="")
        else:
            if inputWord[index] not in usedLetters:
                usedLetters.append(inputWord[index])
            print(Fore.RED+inputWord[index]+Fore.RESET,end="")

    print("\n",usedLetters)
    print("\n")

def validWord(inputWord):
    if len(inputw)!=5:
        return False
    else:
        return True

if validWord(inputWord)==False:
    print("Input is not a 5 letter word.\n")
else:
    checkWord(inputWord,todaysWord)
    guesses-=1

while(inputWord!=todaysWord) and (guesses>0):
    print("Guesses:",guesses)
    inputw = input()
    inputWord = []
    for i in inputw:
        inputWord.append(i)
    
    if validWord(inputWord)==False:
        print("Input is not a 5 letter word.\n")
        continue
    else:
        checkWord(inputWord,todaysWord)
        guesses-=1

if inputWord!=todaysWord:          
    print("You're trash.")
    print("The word was",w)
    print("\n")
else:
    print("You guessed the word!")
    print(w)




