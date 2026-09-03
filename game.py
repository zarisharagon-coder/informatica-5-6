import random

def main():
    guess = ""
    name = input("Whats is ur name?").title()
    print("Hello,",name, "I´m thinking of a number between 1 and 100.Take a guess.")
    cpu = random.randint(1,100)
    while guess != cpu:
        guess= int(input("1-100:"))
        if guess > cpu:
            print("Too high")
        elif guess < cpu:
            print("Too low")
        elif guess == cpu:
            print("U got it!")


if __name__ =="__main__":
    main()
