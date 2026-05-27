import random
import hangmanwords
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
lives=5

word=random.choice(hangmanwords.a)
print(word)
placeholder=""
for i in word:
    placeholder+="_"
print(placeholder)
gameover=False
correctletter=[]
while not gameover:
    guess=input("Enter the guess word:").lower()
   
    display=""
    for i in word:
        if guess==i:
            display+=guess
            correctletter.append(guess)
        elif i in correctletter:
            display+=i
        else:   
            display+="_"
    print(display)
    if guess not in word:
        lives-=1
        print(stages[lives])
    if lives==0:
        print("You lose")
        gameover=True
    if "_" not in display:
        print("You win")
        gameover=True

