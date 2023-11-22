# Python program to list unique characters with their count in a string


def count_unique(str1):
    count = {}

    for char in str1:
        if char.isalnum():
            count[char] = count.get(char , 0) + 1

    return count    

str1 = input("Enter the string: ")    

result  = count_unique(str1)

for char,count1 in result.items():
    if count1>0:
        print(char, count1)
