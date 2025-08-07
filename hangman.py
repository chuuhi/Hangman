import random
words = ['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop',
'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 
'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 
'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider', 
'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language', 
'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus', 
'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful', 
'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard', 
'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser',
'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen',
'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph',
'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'flower',
'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete']

import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses from list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # what current word is (W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: " + " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # takes away a life if wrong
                print("Letter is not in word")

        elif user_letter in used_letters:
            print("You already used that letter. Please try again.")

        else: 
            print("Invalid character. Please try again.")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("Sorry, you died... The word was", word)
    else:
        print("You guessed the word!")


hangman()