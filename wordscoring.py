import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1
   
total = 0
word = input("what word do you want to know the score of?")
for letter in word:
    if letter in values:
        total += values[letter]
print(total, "% for the word ", word)
