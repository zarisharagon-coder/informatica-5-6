def main():
    welcome()
    choice = int(input("Select your oder:"))
    get_item(choice)

def welcome():
    menu = ["Cheeseburger","Fries","Soda","Ice cream","Cookie"]
    print("Welcome to the restaurant!")
    print("Heres the menu")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

def get_item(order):
    kitchen = ["Burger","Fries","Soda","Icecream","Cookie"]
    if 1 <= order <=5:
        print(kitchen(order-1))
    else:
        print("Not in menu")


if __name__ =="__main__":
    main()
