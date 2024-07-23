# Write a funtion in python to read the content from a text file "ABC.txt" line by line and display the same on screen
filename = 'ABC.txt'

with open(filename, 'r') as file:
    for line in file:
        print(line.strip())



# write a function in python to count and display the total number of words in a text file "ABC.txt"
filename = 'ABC.txt'

with open(filename, 'r') as file:
    text = file.read()
    words = text.split()
    total_words = len(words)
    print(f"Total number of words: {total_words}")



# Write a function in python to  count uppercase character in a text file "ABC.txt"
filename = 'ABC.txt'

with open(filename, 'r') as file:
    text = file.read()
    uppercase_count = sum(1 for char in text if char.isupper())

print(f"Total number of uppercase characters: {uppercase_count}")




# write a function display_words() in python to read lines from a text file "story.txt",and display those words,which are less than 4 charcters
filename = 'story.txt'

with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        short_words = [word for word in words if len(word) < 4]
        for word in short_words:
            print(word)