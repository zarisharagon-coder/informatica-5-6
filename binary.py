def main():
    #for example #13 = 1101

    print("Binary to Decimal Converter")
    print("Hello user, this is a Binary to Decimal Converter, you put a binary number and we convert it to decimal!")
    user=(input("Enter a binary number please:"))
    binary_to_decimal(user)


def binary_to_decimal(binary_num):
    decimal = int(binary_num,2)
    print(f"This is your number: {decimal}")
    #when we set something = to an int, when you set the ,2 python counts it as a binary number, I call my stepdad during
    #lunch for help so i really hope i at least pass this test, weve learned avery other function here except of that, the only thing i couldnt do was the error thing



if __name__ =="__main__":
    main()
