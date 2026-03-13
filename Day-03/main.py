print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print("Welcome to treasure island \n")
print("YOur mission is to find the treasure \n")

print("you are at a cross road, where do you want to go \n")


choice=input("type left or right \n")

if choice == "left":
    print("you come to a lake, there is an island in the middle of the lake, type wait to wait for a boat. type swim to swim across \n")
    print("YOu are at a cross road \n")
    choice_1=input("type wait or swim \n")
    if choice== "wait":
        print("You arrive at the island, there is a house with 3 doors, one red, one yellow and one blue, which colour door do you choose")
        choice_2=input("type red, yellow or blue \n")
        if choice_2=="red":
            print("Game over \n")
        elif choice_2=="yellow":
            print("you win \n")
        else:
            print("game over \n")
    else:
        print("YOu attacked , game over \n ")

else:
    print("YOU fell into a hole, game over")
