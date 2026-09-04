import random

def main():
    attempts = 3
    name = input("Whats is ur name?").title()
    print("Hello,",name, " This is EZ math, an easy math learning app,choose how many addittion problems u wanna solve 3-6.")
    dif=int(input("3-6:"))
    if dif == 3:
        correct = 0
        print("Okay so u chose to be simple here is the problem")
        while correct < 3:
            cpu = random.randint(10,99)
            cpu2 = random.randint(10,99)
            print(f"This is the problem {cpu} + {cpu2}")
            answer = int(input("Whats the answer? "))
            if answer == (cpu + cpu2):
                correct += 1
                print("smarty pants")
                print(f"Correct answers::",{correct})
            else:
                print("Wrong, try again")



if __name__ =="__main__":
    main()
