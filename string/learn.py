# To print the number of vowel in a string

s1 = "My name is Aryan Aggarwal. Working as Intern in Wappnet System."
vowel = "aeiou"
count = 0
for char in s1:
    if char.lower() in vowel:
        count+=1

print(count)        



