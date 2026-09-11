import random
words=["python","computer","programming","developer","algorithm"]
word=random.choice(words)
guessed_letters=[]
wrong_guesses=0
max_wrong_guesses=6
display=["_"]*len(word)
hangman_stages=[
"""  +---+
  |   |
      |
      |
      |
=======""",
"""  +---+
  |   |
  O   |
      |
      |
=======""",
"""  +---+
  |   |
  O   |
  |   |
      |
=======""",
"""  +---+
  |   |
  O   |
 /|   |
      |
=======""",
"""  +---+
  |   |
  O   |
 /|\\  |
      |
=======""",
"""  +---+
  |   |
  O   |
 /|\\  |
 /    |
=======""",
"""  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
======="""
]
print("="*45)
print("           HANGMAN GAME")
print("="*45)
print("Guess the hidden word one letter at a time!")
print("You have 6 incorrect guesses.")
print("="*45)
while wrong_guesses<max_wrong_guesses and "_" in display:
    print()
    print(hangman_stages[wrong_guesses])
    print()
    print("Word          :", " ".join(display))
    print("Wrong Guesses :", wrong_guesses, "/", max_wrong_guesses)
    if guessed_letters:
        print("Guessed Letters:", ", ".join(guessed_letters))
    print("-"*45)
    guess=input("Enter a letter: ").lower().strip()
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter exactly one alphabet letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter. Try another!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct! Good guess.")
        for index in range(len(word)):
            if word[index]==guess:
                display[index]=guess
    else:
        wrong_guesses+=1
        print("Wrong guess!")
if "_" not in display:
    print()
    print("="*45)
    print("          CONGRATULATIONS! 🎉")
    print("="*45)
    print("You guessed the word:", word)
    print("Wrong Guesses:", wrong_guesses)
    print("="*45)
else:
    print()
    print(hangman_stages[wrong_guesses])
    print()
    print("="*45)
    print("             GAME OVER")
    print("="*45)
    print("The correct word was:", word)
    print("Better luck next time!")
    print("="*45)
