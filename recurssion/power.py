# power of a function

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

base_input = input("Enter the base: ")
base = int(base_input)

exponent_input = input("Enter the exponent: ")
exponent = int(exponent_input)

result = power(base, exponent)
print(result)