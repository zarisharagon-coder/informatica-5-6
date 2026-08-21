def main():
    print("This pc has 17.8 billion transistors")
    c = 17800000000
    y = int(input("How many years into the future do u want to go ??"))
    t = c*(2**(y/2))

    print("This is how many transistors the pc will have by then", t)
if __name__ =="__main__":
    main()

