# to convert a string with binary digits to integer


digit = input("Enter the binary digit: ")
def bintoint(digit):
    for x in digit:
        if x not in "01":
            return "Not in binary form"
    dig  = int(digit,2)
    return dig


print("binary:{} integer:{}".format(digit,bintoint(digit)))