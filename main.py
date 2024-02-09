import random

words = [
    "TEST",
    "PYTHON",
    "VARIABLE",
    "LOOP",
    "ARRAY", 
    "INTEGER",
    "STRING",
    "FLOAT", 
    "OBJECT",
    "STRING CONCATENATION",
    "CLASS"
]

class word:
    def __init__(self):
        self.w = words[random.randint(0, len(words) - 1)]
        self.currentWord = list(self.w)
        self.guessedChars = []
        print("a new word obj is instantiated")

    def __str__(self):
        return self.w

    def hideWord(self):
        for iw, w in enumerate(self.currentWord):
            if w != " ":
                self.currentWord[iw] = "_"
                    
    def revealLetter(self, user, guess):
        revealedLetters = 0
        for idx, x in enumerate(self.w):
            if x == guess:
                self.currentWord[idx] = guess
                revealedLetters += 1
                user.score += 1
        if revealedLetters == 0:
            self.guessedChars.append(guess)
            user.lives -= 1
                


class player:
    def __init__(self, name) :
        self.name = name
        self.lives = 5
        self.score = 0

def guessWord(user, chosenWord) :
    print(f"HANGMAN\nGuess the Word!\n{chosenWord.currentWord}\nGuessed letters:\n{chosenWord.guessedChars}")
    print(f"Guesses remaining: {user.lives}")
    guess = input("Guess a letter.\n")

    for char in chosenWord.guessedChars:
        if guess == char:
            print(f"Already guessed {guess}, please try again.")
            break

    chosenWord.revealLetter(user, guess)

def main() :

    user = player(input("Thanks for playing Hangman!\nPlease enter a name for our scoreboard!\n"))
    chosenWord = word()

    chosenWord.hideWord()

    while chosenWord.currentWord != list(chosenWord.w):
        if user.lives == 0:
            print("You have run out of guesses.\nGAME OVER")
            # scoreboard here?
            quit()

        guessWord(user, chosenWord)
    
    print(f"Congrats! You won!\nScore:{user.score}")

main()
