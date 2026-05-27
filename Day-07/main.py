import random

from sympy import true
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
wordlist=["india","dubai","thailand"]
rand_word=random.choice(wordlist)
print(rand_word)




empty=""
for i in rand_word:
    empty+="_"
    
print(empty)
  
game_over=False

correctletter=[lives]

while not game_over:
    
    guess=input("Enter the guess word \n").lower()
    empty1=" "   
    for word in rand_word:
        if word == guess:
            empty1+=guess   
            correctletter.append(guess)
        elif word in correctletter:
            empty1+=word
        else:
            empty1+="_"

    print(empty1)
    if guess not in rand_word:
        lives-=1
        print(stages[lives])
        if lives==0:
            game_over=True
            print("You lose")

    if "_" not in empty1:
        print("You win")
        game_over=True

      