import random
from word_list import words
from art import logo,stages

# Get a random word
word = random.choice(words)
# create a variable to track the random word
display = []
end_of_game = False
lives = 6

# display the dashes representing the word
for _ in word:
    display.append("_")

print(logo)
# Display the selected word with blanks 
for dash in display:
    print(dash, end=" ")

# get the user's guess
guess = input("\n\nPlease guess a letter: ").lower()

# if the guess is correct replace the _ in diplay with the guessed letter

for num in range(len(word)):
        if word[num] == guess:
            display[num] = guess
# if the guess is incorrect remove a life
if guess not in word:
    lives -= 1
    print(stages[lives])

    if lives == 0:
        end_of_game = True
        print("You lose!")
print(f" You have {lives} lives remaining")
print(display)
if "_" not in display:
    end_of_game = True
    print("you win!!")