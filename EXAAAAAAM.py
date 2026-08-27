def main():
    l = input("Pick an atmospheric layer")
    if l == "Exosphere":
        print("Your altitude level will be between 700-10,000 km")
        a = int(input("give me your exact altitude in km"))
        t1= 0.5
        print("Total descent time:",a/t1)

    elif l == "Thermosphere":
        print("Your altitude level will be between 85–700 km")
        a = int(input("give me your exact altitude in km"))
        t1= 0.5
        print("Total descent time:",a/t1)
if __name__ =="__main__":
    main()

