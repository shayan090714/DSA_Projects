user_acc_bal = 1000
reply = input("Would you like to Withdraw , Deposit , Check Balance or Exit")
while True:
    if reply == "Withdraw":
        Withdraw_amount = int(input("How much would you like to withdraw?"))
        if Withdraw_amount > user_acc_bal:
            print("Not enough money in account")
        else:
            user_acc_bal = user_acc_bal - Withdraw_amount
            print("You now have",user_acc_bal,"dollars left in your account")
            reply = input("Would you like to Withdraw , Deposit , Check Balance or Exit")
    if reply == "Deposit":
        Deposit_amount = int(input("How much money would you like to deposit?"))
        user_acc_bal = user_acc_bal + Deposit_amount
        print("You now have",user_acc_bal,"dollars in your account")
        reply = input("Would you like to Withdraw , Deposit , Check Balance or Exit")
    if reply == "Check Balance":
        print("You have",user_acc_bal,"dollars in your account")
        reply = input("Would you like to Withdraw , Deposit , Check Balance or Exit")
    if reply == "Exit":
        print("Have a nice day")
        break