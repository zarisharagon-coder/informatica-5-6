def main():
    planet= input("Planet: ")
    # Separation
    print("Hello", planet)


    #Ending
    print("Hello", end= " ")
    print (planet)

    # Concatemation
    print("Hello " + planet)

    #Formatig String
    print(f"Hello {planet}")

if __name__ =="__main__":
    main()
