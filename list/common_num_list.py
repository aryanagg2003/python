# to find common numbers in 2 list

lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
lst3 = []

for char1 in lst1:
    if char1 in lst2:
        lst3.append(char1)

print(lst3)
