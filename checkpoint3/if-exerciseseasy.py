def main():
    num = int(input("Pick any number:"))
    if num >= 0:
        print(num)
    elif num <= 0:
        num = num*-1
        print(num)


if __name__ =="__main__":
    main()
