def main():
    l = input("Pick an atmospheric layer")
    if l == "Exosphere":
        print("Your altitude level will be between 700-10,000 km")
        a = float(input("give me your exact altitude in km"))
        t1= 2
        print("Total descent time:",(a-9300)/t1+((a-12)/0.02)+((a-50)/0.075)+((a-85)/0.2)+((a-615)/0.5),"s")
    elif l == "Thermosphere":
        print("Your altitude level will be between 85–700 km")
        a = float(input("give me your exact altitude in km"))
        t1= 0.5
        print("Total descent time:",(a-615)/t1+((a-12)/0.02)+((a-38)/0.075)+(a-35)/0.2,"s")
    elif l == "Mesosphere":
        print("Your altitude level will be between 50–85 km")
        a = float(input("give me your exact altitude in km"))
        t1= 0.2
        print("Total descent time:",(a-35)/t1+((a-12)/0.02)+((a-38)/0.075),"s")
    elif l == "Stratosphere":
        print("Your altitude level will be between 12-50 km")
        a = float(input("give me your exact altitude in km"))
        t1= 0.075
        print("Total descent time:",(a-50)/t1+(a-12)/0.02,"s")
    elif l == "Troposphere":
        print("Your altitude level will be between 0-12 km")
        a = float(input("give me your exact altitude in km"))
        t1= 0.02
        print("Total descent time:","s")
    else:
        print(c)
if __name__ =="__main__":
    main()

