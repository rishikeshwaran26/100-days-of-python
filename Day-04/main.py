import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rand_num=random.randint(0,2)

choice=input("What do you choose type 0 fro rock, 1 for paper and 2 for scissors \n")

print(rand_num)

print("Computer chose:")
if rand_num==0:
    print(rock)
elif rand_num==1:
    print(paper)
elif rand_num==2:
    print(scissors)
else:
    print("wrong input")

print("you chose:")

if choice=="0":
    print(rock)
    if rand_num==0:
        print("Its draw")
    elif rand_num==2:
        print("You win")
    else:
        print("You lose")   
elif choice=="1":
    print(paper)
    if rand_num==1:
        print("Its draw")
    elif rand_num==0:
        print("You win")
    else:
        print("You lose")   
elif choice=="2":
    print(scissors)
    if rand_num==2:
        print("Its draw")
    elif rand_num==1:
        print("You win")
    else:
        print("You lose")   
else:
    print("wrong input")

