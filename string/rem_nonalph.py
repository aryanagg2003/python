# Python program to remove all non-alphabetic characters from a string

str1 = "my na1m@ i2 Ar#6a_n"
str2 = ''

for char in str1:
    if char.isalpha() or char.isspace():
        str2 += char

print(str2)