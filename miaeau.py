# Open the file and read each line
with open("youtube.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Strip whitespace and print each book name
        print(line.strip())





sleepy_person= input("are you sleeping?")
if sleepy_person== "yes":
    print("go to sleep")
elif sleepy_person== "no" :
    print("stay in class")
# you are telling the user to print sleppy or not
else:
    print("you can only write yes or no")    






sleepy_person= input("are you sleeping?")
if sleepy_person== "yes":
    print("go to sleep")
elif sleepy_person== "no" :
    print("stay in class")
# you are telling the user to print sleppy or not
else:
    print("you can only write yes or no")    

def mad_libs():
    # Get user input
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb1 = input("Enter a verb: ")
    exclamation = input("Enter an exclamation: ").capitalize()  # Capitalize automatically
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter one more verb: ")

    # Story with user inputs
    story = (f"The other day, I was really in trouble. It all started when I saw a very "
             f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. "
             f"But all I could think to do was to {verb2} over and over. Miraculously, "
             f"that caused it to stop, but not before it tried to {verb3} "
             f"right in front of my family.")

    # Print the final story
    print("\nHere is your funny story:\n")
    print(story)

# Run the program
mad_libs()
def mad_libs():
    # Get user input
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb1 = input("Enter a verb: ")
    exclamation = input("Enter an exclamation: ").capitalize()  # Capitalize automatically
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter one more verb: ")

    # Story with user inputs
    story = (f"The other day, I was really in trouble. It all started when I saw a very "
             f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. "
             f"But all I could think to do was to {verb2} over and over. Miraculously, "
             f"that caused it to stop, but not before it tried to {verb3} "
             f"right in front of my family.")

    # Print the final story
    print("\nHere is your funny story:\n")
    print(story)

# Run the program
mad_libs()
