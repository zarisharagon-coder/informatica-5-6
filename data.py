def main():
    width = int(input("Enter the width of the rectangle: "))
    print("0" * width)
    print("0" * width)
    print("0" * width)
    print("0" * width)
    print("0" * width)
    p = (5*2)+ (width*2)
    print("perimeter:", p)
    a = (width*5)
    print("area:", a)
    diagonal = ((5**2)+(width**2))**0.5
    print("diagonal", diagonal)
if __name__ =="__main__":
    main()
