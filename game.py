import random

def main():
    attempts = 3
    guess = ""
    name = input("Whats is ur name?").title()
    print("Hello,",name, "pick a difficulty level, 1 2 or 3.")
    dif=int(input("1-3:"))
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
                print("U got it!",name)
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
                print("U got it!",name)

    elif dif == 3:
        print("dang,",name, "you took the challenge, pick a number between 1 - 100.")
        cpu = random.randint(1,100)
        while attempts > 0:
            guess= int(input("1-100:"))
            if guess > cpu:
                print("Too high")
                attempts -=1
                print("Attempts left",attempts)
            elif guess < cpu:
                print("Too low")
                attempts -=1
                print("Attempts left",attempts)
            elif guess == cpu:
                print("U got it!",name)

    else:
        print("ERORR")
if __name__ =="__main__":
    main()
