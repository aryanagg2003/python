# to sort a list of strings on the number of alphabets in each word.

lst = ['apple', 'banana', 'kiwi', 'orange', 'grape']

lst1 = list(sorted(lst,key = lambda x: len(x)))

print(lst1)