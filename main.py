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
    "CLASS"
]

class word:
    def __init__(self):
        self.w = words[random.randint(0, len(words) - 1)]

    def __str__(self):
        return self.w

    def breakDownWord(self) :
        return list(self.w)

    def hideWord(self) :
        self.currentWord = self.w

        for i in self.currentWord:
            self.currentWord[i] = "_"

    def revealLetter(self, guess) :
        for i in self.w:
            if self.w[i] == guess:
                self.currentWord[i] = guess
            else:
                player.lives - 1


class player:
    def __init__(self, name) :
        self.name = name
        self.lives = 5
        self.score = 0

name = input("Thanks for playing Hangman!\nPlease enter a name for our scoreboard!")

