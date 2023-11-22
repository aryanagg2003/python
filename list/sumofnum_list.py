# to find sum of all numbers in a list.

L1 = [1, 9, 1, 6, 3, 4]
ttl = 0
for x in L1:
   ttl+=x
print ("Sum of all numbers Using loop:", ttl)
ttl = sum(L1)
print ("Sum of all numbers sum() function:", ttl)