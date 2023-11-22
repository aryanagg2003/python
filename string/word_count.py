# Python program to find number of words in a string

str1 = "Python programming is fun and versatile"
count = 1

for char in str1:
    if char == ' ':
        count += 1

print(count)