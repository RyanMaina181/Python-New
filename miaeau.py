# Open the file and read each line
with open("youtube.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Strip whitespace and print each book name
        print(line.strip())




