import random
num1 = random.randint(0,4)
num2 = random.randint(5,9)
num3 = random.randint(3,7)
chances = 4
print("This is a safe.For each digit,you have 4,3,and 2 chances to figure out the 1st,2nd,and 3rd digit respectively.Else,the safe will auto lock.")
while not chances == 0:
    ans1 = int(input("The first number is between 0 and 4.What is the first number?"))
    if num1 == ans1:
        print("Correct!")
        chances = 3
        break
    else:
        chances=chances-1
        print("Wrong!The amount of chances you have left is",chances,".")
else:
    print("Safe is locked.")
while not chances == 0:
    ans2 = int(input("The second number is between 5 and 9.What is the second number?"))             
    if num2 == ans2:
        print("Correct!")
        chances = 2
        break
    else:
        chances=chances-1
        print("Wrong!The amount of chances you have left is",chances,".")
else:
    print("Safe is locked.")
while not chances == 0:
    ans3 = int(input("The third number is between 0 and 9.What is the third number?"))
    if num3 == ans3:
        print("You have unlocked the safe!")
        break
    else: chances=chances-1
    print("Wrong!The amount of chances you have left is",chances,".")
else:
    print("Safe is locked.")