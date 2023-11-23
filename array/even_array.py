# to store all even numbers from an array in another array

arr_input = input("Enter the array: ")

arr = [int(x) for x in arr_input.split()]

arr1 = []

for i in range(len(arr)):
    if arr[i]%2==0:
        arr1.append(arr[i])

print(arr1)