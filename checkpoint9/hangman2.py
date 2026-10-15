else:
import random
if "_" not in hint:
attempts -= 1
start_game("words.txt")
if guess in word and guess not in hint:
for i in range(len(word)):
print(f"Incorrect letters: {" ".join(incorrect_letters)}")
break
main()
print("Congratulations! 🥳 You guessed the word:", word)
print("Wrong guess! Attempts left:", str(attempts))
incorrect_letters.append(guess)
if attempts == 0 and "_" in hint:
print("You already guessed that letter! Attempts left:", str(attempts))
if len(guess) == 1:
print("No attempts left 💀 The word was:", word)
attempts -= 1
else:

