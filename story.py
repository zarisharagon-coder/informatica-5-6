def main():
#     planet= input("Planet: ")
#     # Separation
#     print("Hello", planet,)


#     #Ending
#     print("Hello", end= " ")
#     print (planet)

#     # Concatemation
#     print("Hello " + planet)

#     #Formatig String
#     print(f"Hello {planet}")

    name= input("What is your name? ").title().strip()
    color= input("Tell me a color: ").lower().strip()
    adj= input("Tell me an adjetive ").lower().strip()
    goal= input("A goal you would like to achieve").lower().strip()

    print("Hello", name)
    print("This is your story")
    print(f"At dawn the sky turned {color} , and the air felt {adj}. I decided today I will finally learn to {goal}")
    print(f"At dawn the sky turned {color} , and the air felt {adj}. I decided today I will finally learn to {goal}.".upper())

if __name__ =="__main__":
    main()
