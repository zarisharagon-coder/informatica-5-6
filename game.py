import random

def main():
    guess = ""
    name = input("Whats is ur name?").title()
    print("Hello,",name, "pick a difficulty level, 1 2 or 3.")
    dif=int(input("1-3"))
    if dif == 1:
        print("Hello,",name, "I´m thinking of a number between 1 and 10.Take a guess.")
        cpu = random.randint(1,10)
        while guess != cpu:
            guess= int(input("1-10:"))
            if guess > cpu:
                print("Too high")
            elif guess < cpu:
                print("Too low")
            elif guess == cpu:
                print("U got it!")
    elif dif == 2:
        print("Hello,",name, "I´m thinking of a number between 1 and 50.Take a guess.")
        cpu = random.randint(1,50)
        while guess != cpu:
            guess= int(input("1-50:"))
            if guess > cpu:
                print("Too high")
            elif guess < cpu:
                print("Too low")
            elif guess == cpu:
                print("U got it!")

    elif dif == 3:
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
