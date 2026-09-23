def main():
    num = int(input("What table do you want to learn? (1-10)"))
    print(f"okey, we will learn the table of {num}")
    if num >= "10":
        print("1-10, TRY AGAIN")
    if num <= "1":
        print("1-10, TRY AGAIN")


    print(f"""
{num} times 1 is {1*num}
{num} times 2 is {2*num}
{num} times 3 is {3*num}
{num} times 4 is {4*num}
{num} times 5 is {5*num}
{num} times 6 is {6*num}
{num} times 7 is {7*num}
{num} times 8 is {8*num}
{num} times 9 is {9*num}
{num} times 10 is {10*num}""")


if __name__ =="__main__":
    main()
