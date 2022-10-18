import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

while True:
    total = 0
    word = input("what word do you want to know the score of?")
    if word == "0":
        break
    else:
        for letter in word.lower():
            if letter in values:
                total += values[letter]
        print(total, "% for the word ", word)