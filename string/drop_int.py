# to drop all digits from a string

str = 'He12llo, Py00th55on!'
char = ''

for x in str:
    if not x.isdigit():
        char += x
print("the final string is {}".format(char))