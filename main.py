import random
import words
import HangmanArt

words_list = words.word_list
word = random.choice(words_list).lower()
eachLetter = list(word)
stages = HangmanArt.stages

lives = len(stages)

blanks = []

target = int(len(eachLetter)) 

for n in range(target):
    blanks.append("_")


guessedLetters= []

while "_" in blanks and lives > 0:
    guess = input("Guess a letter:\n").lower()
    
    for n in range(target):
        if guess == eachLetter[n]:
            if guess not in guessedLetters:
                guessedLetters.append(guess)
            blanks[n] = guess
    if guess not in eachLetter:
        print("You guessed {guess}, it isn't in the word")
        if guess not in guessedLetters:
            lives -= 1
            print(stages[lives])
            print(f"Lives left: {lives}")
            guessedLetters.append(guess)
        else:
            print(guess)
            print(f"Already guessed this letter! Here's your guesses: {guessedLetters}")
    print(blanks)

if not "_" in blanks:
    print("Congratulations, you've won")

if lives <= 0:
    print("Sorry, you lose!")