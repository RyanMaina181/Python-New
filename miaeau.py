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



