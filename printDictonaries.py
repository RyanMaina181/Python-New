smartphone={
    "brand":"samsung",
    "number":"25",
    "year" :"2025",
     "color":"rainbow"
}
print(smartphone)

print(smartphone["number"]) 



color = input("What is your favorite color? ")

# This if statement will only match "blue" not "Blue" or "BLUE"
if color == "blue":
    print("I like blue too.")


# This if statement will match the word blue, regardless of the capitalization
if color.lower() == "blue":
    print("I like blue too.")

    
# Ask the user for two integers
num10 =input("Enter the first integer: ")
num27 = input("Enter the second integer: ")
if num10 > num27 :
   print(f"{num10} is  greater than {num27}")
else:
    print(f"{num27} is  greater than {num10}")


    

# Compare if the first number is greater than the second


# Compare if the two numbers are equal

# Compare if the second number is greater than the first


# Comparing Strings
# Ask the user for their favorite animal
favorite_animal = input("What is your favorite animal? ").lower()

# Define the programmer's favorite animal
my_favorite_animal = "dog"

# Check if the user's favorite animal is the same as the programmer's
if favorite_animal == my_favorite_animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite")







num =int(input ("put a number"))

if num > 12 :
    print("i am  a person")
  
    
    for i in range(2, (num//2)+1):
      
        
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")



items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

for item in items:
    print(f"The item is: {item}") 



for num in range(1, 21, 2):  # Start at 1, stop at 20, step by 2
    print(num)




# Part 1: Display each color on a new line
colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(color)

print()  # Adds a blank line for better readability

# Part 2: Display numbers 1 to 8, each on a new line
for num in range(1, 9):
    print(num)

print()  # Adds a blank line for better readability

# Part 3: Display even numbers from 2 to 20
for num in range(2, 21, 2):
    print(num)


# Ask the user for their favorite letter
favorite_letter = input("What is your favorite letter? ").lower()

# Define the word to loop through
word = "Commitment"

# Loop through each letter in the word
for letter in word:
    # Check if the letter matches the favorite letter (case insensitive)
    if letter.lower() == favorite_letter:
        print("_", end="")  # Hide the letter
    else:
        print(letter, end="")  # Print the letter as is

print()  # Print a newline after output






import random

# List of words to choose from
words = ["python", "flask", "django", "react", "tensorflow", "developer"]

# Choose a random word
word_to_guess = random.choice(words)
word_display = ["_"] * len(word_to_guess)  # Placeholder for guessed letters
attempts = 4000 # Maximum attempts allowed
guessed_letters = set()  # Store guessed letters

print("Welcome to the Word Guess Game!")
print("Try to guess the word, one letter at a time.")
print(" ".join(word_display))

while attempts > 0 and "_" in word_display:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_to_guess:
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                word_display[index] = guess
        print("Correct! ", " ".join(word_display))
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

if "_" not in word_display:
    print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("\n😞 Out of attempts! The word was:", word_to_guess)
9




   



















