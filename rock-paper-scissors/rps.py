import random

print("===================")
print("Rock Paper Scissors")
print("===================") 
print("1) ✊")
print("2) ✋")
print("3) ✌️")

player = input("Choose a number: ")
computer = random.randint(1,3)

match player:
    case "1":
        print("You chose: ✊")
    
    case "2":
        print("You chose: ✋")

    case "3":
        print("You chose: ✌️")

    case _:
        print("Invalid number")
        
if player in ["1", "2", "3"]:
    match computer:
        case 1:
            print("Computer chose: ✊") 
    
        case 2:
            print("Computer chose: ✋")

        case 3:
            print("Computer chose: ✌️")

if player == "1" and computer == 1 or player == "2" and computer == 2 or player == "3" and computer == 3:
    print("It is a tie")

elif player == "1" and computer == 2:
    print("Computer Won")

elif player == "1" and computer == 3:
    print("Player Won")

elif player == "2" and computer == 1:
    print("Player Won")

elif player == "2" and computer == 3:
    print("Computer Won")

elif player == "3" and computer == 1:
    print("Computer Won")

elif player == "3" and computer == 2:
    print("Player Won")