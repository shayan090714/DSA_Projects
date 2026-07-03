import random
level = 1
high_score = 0
while True:
    php = 100
    ehp = 80 + (level - 1) * 20  
    Super_Attack_Used = False
    if level >= 2:
        print("You are battling an even STRONGER monster than the previous one.")
    else:
        print("You are battling a monster.")
    e_attack = ["Bite","Smash","Roar","Heal"]
    while php > 0 and ehp > 0:
        print("You can either Attack,Super Attack,Heal,or Run")
        p_attack = str(input("What will you do?"))
        if p_attack == "Attack":
            p_damage = random.randint(10,15)
            print("You choose Attack!")
            print("You deal",p_damage,"damage to the enemy!")
            ehp = ehp - p_damage
            print("Enemy's health is",ehp)
            if ehp <= 0:
                print("You win!")
                print("You completed level",level)
                level = level + 1
                print("Level",level,"reached!")
                break
            input("Press Enter to continue...")
        elif p_attack == "Super Attack":
            if Super_Attack_Used:
                print("You can't use this again")
                continue
            else:
                Super_Attack_Used = True
                p_damage = random.randint(20,30)
                print("You choose Super Attack!")
                print("You deal",p_damage,"damage to the enemy!")
                ehp = ehp - p_damage
                print("Enemy's health is",ehp)
                if ehp <=0:
                    print("You win!")
                    print("You completed level",level)
                    level = level + 1
                    print("Level",level,"reached!")
                    break
                input("Press Enter to continue...")
        elif p_attack == "Heal":
            php = php + 10
            print("You choose Heal!")
            print("Your health increases by 10!")
            print("Your health is",php)
            print("Enemy's health stays the same.")
            input("Press Enter to continue...")
        elif p_attack == "Run":
            print("You run!")
            ran_away = True
            exit()
        else:
            print("Invalid choice!")
            continue
        if not php > 0 and ehp > 0:
            enemy_attack = random.choice(e_attack)
            if enemy_attack == "Bite":
                e_damage = random.randint(5 + level, 10 + level)
                print("Enemy chose Bite!")
                print("Enemy deals",e_damage,"damage to you!")
                php = php - e_damage
                print("Your health is",php)
                if php <= 0:
                    print("You lose!")
                    print("You lost at level",level)
                    score = level
                    if score > high_score:
                        high_score = score
                        print("Your new high score is",score,".Congratulations!")
                    else:
                        print("Your score is",score,".Better luck next time!")
                    exit()
            elif enemy_attack == "Smash":
                    e_damage = random.randint(8 + level, 13 + level)
                    print("Enemy chose Smash!")
                    print("Enemy deals",e_damage,"damage to you!")
                    php = php - e_damage
                    print("Your health is",php)
                    if php <= 0:
                        print("You lose!")
                        print("You lost at level",level)
                        score = level
                        if score > high_score:
                            high_score = score
                            print("Your new high score is",score,".Congratulations!")
                        else:
                            print("Your score is",score,".Better luck next time!")
                        exit()
            elif enemy_attack == "Roar":
                print("Enemy chose Roar!")
                print("Its so loud it deals 5 damage to you!")
                php = php - 5
                print("Your health is",php)
                if php <= 0:
                        print("You lose!")
                        print("You lost at level",level)
                        score = level
                        if score > high_score:
                            high_score = score
                            print("Your new high score is",score,".Congratulations!")
                        else:
                            print("Your score is",score,".Better luck next time!")
                        exit()
            elif enemy_attack == "Heal":
                print("Enemy chose Heal!")
                print("Enemy's health increases by 10!")
                ehp = ehp + 10
                print("Enemy's health is",ehp)
                continue