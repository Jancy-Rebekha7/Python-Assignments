# Exercise 1: Perform Basic Set Operations 


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Exercise 2: Union of Sets 

print(A | B)

# or 
print(A.union(B))

# Exercise 3: Intersection of Sets

print(A & B)

# or 
print(A.intersection(B))

# Exercise 4: Difference of Sets 

print(A - B)
# or 
print(A.difference(B))

# Exercise 5: Symmetric Difference 

print(A ^ B)
# or
print(A.symmetric_difference(B))

# Exercise 6: Add a list of Elements to a Set 


A.add(7)
print(A)

# Exercise 7: Set Difference Update


A = {1, 2, 3, 4}
B = {3, 4, 5}

# Remove elements from A that are also in B
A.difference_update(B)

print(A)

# Exercise 8: Remove Items From Set Simultaneously

A = {1, 2, 3, 4, 5, 6}

for item in [2, 4, 6]:
    A.discard(item)

print(A)

# Exercise 9: Check Subset 


A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))

# or 
print(A <= B)

# Exercise 10: Check Superset 


A = {1, 2, 3, 4}
B = {2, 3}
print(A.issuperset(B))

# Exercise 11: Set Intersection Check 


A = {1, 2, 3}
B = {3, 4, 5}


result = A.intersection(B)

print(result)

# Exercise 12: Set Symmetric Difference Update 


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


A.symmetric_difference_update(B)

print(A)

# Exercise 13: Set Intersection Update


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


A.intersection_update(B)

print(A)

# Exercise 14: Find Common Elements in Two Lists


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]


common = list(set(list1) & set(list2))

print(common)

# Exercise 15: Frozen Set 


fs = frozenset([1, 2, 3, 4])

print(fs)

# Exercise 16: Count Unique Words 


sentence = "python is easy and python is powerful"

# Split sentence into words
words = sentence.split()

# Get unique words using set
unique_words = set(words)

# Count unique words
count = len(unique_words)

print("Unique words:", unique_words)
print("Count:", count)



