# to remove duplicate characters from a string

string_with_duplicates = "programming is fun and challenging"
str1 = ' '

for x in string_with_duplicates:
    if x not in str1:
        str1 += x
    elif x == ' ':
        str1 += x

print("removed duplicates string is: ",str1)