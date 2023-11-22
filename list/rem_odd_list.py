#  to remove all odd numbers from a list.

input_string = input("Enter a list of integers separated by spaces: ")
my_list = list(map(int, input_string.split()))
list1=[]
for x in my_list:
    if x%2==0:
        list1.append(x)

print(list1)