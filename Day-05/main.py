import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator")
letter=int(input("How many letters would you like to generate in password \n"))
number=int(input("How many numbers would you like to generate in password \n"))
symbol=int(input("How many symbols would you like to generate in password \n"))

password=[]

for i in range(1,letter+1):
    password+=random.choice(letters)
for i in range(1,number+1):
    password+=random.choice(numbers)
for i in range(1,symbol+1):
    password+=random.choice(symbols)

random.shuffle(password)


final_password=""
for char in password:
    final_password+=char
print(f"Your password is {final_password}")