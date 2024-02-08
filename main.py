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
        self.currentWord = self.w
        self.guessedChars = []

    def __str__(self):
        return self.w

    def breakDownWord(self) :
        return list(self.w)

    def hideWord(self) :
        for i in self.currentWord:
            if self.currentWord[i] != " ":
                self.currentWord[i] = "_"

    def revealLetter(self, user, guess) :
        for i in self.w:
            if self.w[i] == guess:
                self.currentWord[i] = guess
                user.score += 1
            else:
                self.guessedChars.append(guess)
                user.lives -= 1


class player:
    def __init__(self, name) :
        self.name = name
        self.lives = 5
        self.score = 0

def guessWord(chosenWord) :
    print(f"HANGMAN\nGuess the Word!\n{chosenWord.currentWord}\nGuessed letters:\n{chosenWord.guessedChars}")
    guess = input("Guess a letter.")

    for i in chosenWord.guessedChars:
        if guess == chosenWord.guessedChars[i]:
            print(f"Already guessed {guess}, please try again.")
            guessWord(chosenWord)

    chosenWord.revealLetter(guess)

def main() :

    user = player(input("Thanks for playing Hangman!\nPlease enter a name for our scoreboard!\n"))
    chosenWord = word()

    chosenWord.breakDownWord()
    # need to break down current word without breaking down chosen word?
    chosenWord.hideWord()

    for i in range(26):
        if user.lives == 0:
            print("You have run out of guesses.\nGAME OVER")
            quit()

        if chosenWord.currentWord ==
        guessWord(chosenWord)

# main()



