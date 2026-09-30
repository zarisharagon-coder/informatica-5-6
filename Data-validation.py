def main ():
    #3number = input("Enter a number.") #"1"
    try:
        number = int(input("Enter a number")) #1
        print("Number stored succesfully.")
    except ValueError:
        print("You didnt entered a number")


if __name__ =="__main__":
    main()
