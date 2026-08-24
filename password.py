def main():
    password = "infobetterthanconta?"
    print("💡")
    attempt = input("Insert ur guess,")
    if attempt == password:
        print("Congrats, u know ball")
    if attempt != password:
        print("Loser, try again")
        print("BYEEEEE")
if __name__ =="__main__":
    main()
