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
    start_game("listword.txt")
def start_game(letters):
    with open(letters) as words:
        listwords = words.read().splitlines()
    word = random.choice(listwords)
    print(word)
if __name__ =="__main__":
    main()
