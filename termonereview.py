from datetime import datetime

def main():
    day = datetime.now().weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Saturday"]
    print(days [day])
    if day < 4:
        print(day)
        print("Its a weekday")
        remaining = 5 - day
        print(f"{remaining} days until weekend")
    elif day == 4:
        print("Its a friday")
        print("Juar a day lefr until the weekend")
    else:
        print("Its a weekend!")
    months = ["January", "February", "March","April","May","June","July","August","September","November","December"]
    print(months[5])
    print(months[6])
    print(months[7])


if __name__ =="__main__":
    main()
