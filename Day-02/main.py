print("Welcome to the tip calculator \n")
tot_bill=int(input("What was the total bill \n"))
tip=int(input("how much tip would you like to give?10,12,15 \n"))
split=int(input("How many people to split bill"))
each_split=((tot_bill+tip)/split)
print(f"The split for each person is {each_split}")

