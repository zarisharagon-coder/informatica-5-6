def main ():
    not_validated = True
    while not_validated:
    #number = input("Enter a number.") #"1"
        try:
            number = int(input("Enter an interger number:")) #1
            print("Number stored succesfully.")
            not_validated = False #same st as break
        except ValueError:
            print("You didnt entered a number😭:")


if __name__ =="__main__":
    main()
