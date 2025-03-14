kindiki=5.78
gachagua=8.99
if gachagua > kindiki:
    print ("ruto must go")
ruto=list (("apple","ali"))
if "ali" in ruto:
    ruto.remove("ali")
    print(ruto)


popppppppppppppppppppp=list(("maina","emannuel","petit"))
popppppppppppppppppppp.clear()
print(popppppppppppppppppppp)
potty = list(("dadda", "mama", "ryan"))
potty.pop(-1)
print(potty)

import random

# The computer picks a random number between 1 and 100
magic_number = random.randint(1, 100)

print("Welcome to the Guess My Number game!")
print("I'm thinking of a number between 1 and 100.")

# Initialize the guess variable
guess = None

# Loop until the user guesses the correct number
while guess != magic_number:
    try:
        # Get user input
        guess = int(input("Take a guess: "))

        # Check if the guess is correct
        if guess < magic_number:
            print("Higher! Try again.")
        elif guess > magic_number:
            print("Lower! Try again.")
        else:
            print("Congratulations! You guessed the magic number.")
    except ValueError:
        print("Please enter a valid number.")


