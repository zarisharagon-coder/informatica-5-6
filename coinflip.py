import random

def main():
    guess= int(input("1 for heads or 2 for tails????"))
    head = random.randint(1,2)
    if (head) == 1:
        print("Heads")
    elif (head) == 2:
        print("Tails")
    if head == guess:
        print("U go it")
    elif head != guess:
        print("TaiLs,loser")
if __name__ =="__main__":
    main()
