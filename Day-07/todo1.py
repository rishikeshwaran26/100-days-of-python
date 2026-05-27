import random
from hangmanwords import a
from stages import stages,logo
lives=5

logo = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

print(logo)

word=random.choice(a)
print(word)
placeholder=""
for i in word:
    placeholder+="_"
print(placeholder)
gameover=False
correctletter=[]
while not gameover:
    guess=input("Enter the guess word:").lower()
    if guess in correctletter:
        print(f"You have already guessed this letter: {guess}")
        
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

