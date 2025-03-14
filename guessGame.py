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
    print("\n Congratulations! You guessed the word:", word_to_guess)
else:
    print("\n Out of attempts! The word was:", word_to_guess)



def display_menu():
    print("\nShopping Cart Menu:")
    print("1. Add a new item")
    print("2. Display the contents of the shopping cart")
    print("3. Quit")

def add_item(cart):
    item = input("Enter the name of the item: ")
    cart.append(item)
    print(f"'{item}' has been added to your cart.")

def display_cart(cart):
    if not cart:
        print("Your shopping cart is empty.")
    else:
        print("\nShopping Cart Contents:")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item}")

def main():
    cart = []  # List to store item names
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_item(cart)
        elif choice == "2":
            display_cart(cart)
        elif choice == "3":
            print("Thank you for using the shopping cart program!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()    
9




   



















