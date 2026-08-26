def main():
    num = int(input("Pick any number:"))
    num2 = int(input("Pick A SECOND number:"))
    pick =int(input("What do u want to do (1:add,2:subtract,3:Multiply,4:divide):"))
    if pick == 1:
        print(num+num2)
    elif pick == 2:
        print(num-num2)
    elif pick == 3:
        print(num*num2)
    elif pick == 4:
        print(num/num2)
    else:
        print("I SAID 1-5")

if __name__ =="__main__":
    main()
