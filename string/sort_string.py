# to sort the string"

my_string = "python is fun"


str = ' '.join(sorted(my_string.split() , key = str.lower))

print(str)