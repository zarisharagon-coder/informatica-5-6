# Create a TXT file with all of the words
#Define the main function
#define some values beforehand
#add a print
#explain the game
#create a loop
#use the with function to open the txt file
#ask the user for a letter
#store the letter in a list
#add a countdown that will act as lifes
#compare the letters on the list to the one word selected
#put a random to choose the word
#if functions
# If they loose then print a womp womp
# if they win print a "Correct!" and display a word
#
import random
def main():
    start_game("words.txt")
def start_game(file):
    attempts = 10
    with open(file) as f:
        word_bank = f.read().splitlines()
    word = random.choice(word_bank).lower()
    incorrect_letters = []
    hint = ["_"] * len(word)
    while attempts > 0:
        print("Current word:", " ".join(hint))
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
                break
            else:
                print("Invalid guess. Try again.")
        if guess not in incorrect_letters:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            print("Great guess!")
        elif guess in hint:
            attempts -= 1
            print("You already guessed that letter! Attempts left:", str(attempts))
        else:
            attempts -= 1
            print("Wrong guess! Attemps left:", str(attempts))
            if guess not in incorrect_letters:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")
            break
        if attempts == 0 and "_" in hint:
            print("No attempts left!")

            break








if __name__ =="__main__":
    main()
