#  to find the largest number in an array
size = int(input("Enter the size of array: "))
arr = []

for i in range(size):
    element = int(input("Enter the elements in array: "))
    arr.append(element)

largest = arr[0]

for j in range(1, len(arr)):
    if arr[j] > largest:
        largest = arr[j]

print("The largest number in the array is:", largest)


