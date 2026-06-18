import random 

number = random.randint(1,100)
counter = 0

while True:
    try:
        guess = int(input("Guess the number: "))
        counter += 1
        if guess > number:
            print("Too High")

        elif guess < number:
            print("Too Low")

        else:
            print("You got it")
            print(f"Tries: {counter}")
            break
    except ValueError:
        pass