#reverse string 

def reverse_string(s):
    if not s:
        return s
    return s[-1] + reverse_string(s[:-1])

str = input("enter the string: ")
print(reverse_string(str))
