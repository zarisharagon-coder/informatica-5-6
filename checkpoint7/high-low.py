def main():
    #defining functio 1
    def highest(a,b):
        if a > b:
            highest_num = a
        elif b > a:
            highest_num = b

        print((f"The highest number entered is {highest_num}"))

    highest(8,2)
    num1=int(input("Give me a number:"))
    num2=int(input("Give me a second number:"))
    highest(num1,num2)

    def lowest (a,b,c):
        if a < c and a < b:
            lowest_num = a
        elif b < c and b < a:
            lowest_num = b
        elif c < a and c < b:
            lowest_num = c

        print((f"The lowest number entered is {lowest_num}"))

    num1=int(input("Give me a number:"))
    num2=int(input("Give me a second number:"))
    num3=int(input("Give me a third number:"))
    lowest(num1,num2,num3)





if __name__ =="__main__":
    main()
