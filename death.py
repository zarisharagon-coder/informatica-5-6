import time
def main():
    n = input("Hello, whats ur name?:")
    print(f"Hello {n} this app is designed to set up an alarm for when u bake")
    at = float(input("How long is ur timer? (p.s set the time in minutes):"))
    start=input("Type start:")

    if start == "start":
        seconds = at * 60
        while seconds > 0:
            print(seconds)
            time.sleep(1)
            seconds -= 1
        print("Times up!")



if __name__ =="__main__":
    main()
