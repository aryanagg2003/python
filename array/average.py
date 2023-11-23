# to find the average of all numbers in a Python array

arr_input = input("enter the array")

arr = [int(x) for x in arr_input.split()]
total = 0

for i in range(len(arr)):
    total += arr[i]

average = total/len(arr)
print(average)

