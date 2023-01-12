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