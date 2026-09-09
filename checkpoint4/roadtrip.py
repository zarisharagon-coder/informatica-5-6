def main():
    answer = "" #Initialize
    followup= ""

    while answer != "Yes!": #condition
        answer = input("Are we there yet?").strip().title() #update
        if answer == "Yes":
            followup = input("Really?").strip().title()
        if followup == "Yes!":
            break


    print("We just arrived")

if __name__ =="__main__":
    main()
