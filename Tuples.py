# Exercise 1: Perform Basic Tuple Operations

my_tuple = (10, 20, 30, 40, 50)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:4])
print(20 in my_tuple)

# Exercise 2: Tuple Repetition 


t = (1, 2, 3)

# Repeat tuple 3 times
result = t * 3

print(result)

# Exercise 3: Slicing Tuples

print(my_tuple[1:4])

# Exercise 4: Reverse the tuple


reversed_tuple = t[::-1]
print(reversed_tuple)

# or


reversed_tuple = tuple(reversed(t))
print(reversed_tuple)

#Exercise 5: Access Nested Tuples 

t = (1, 2, (3, 4, 5), 6)

print(t[2])
print(t[2][0])

# Exercise 6: Create a tuple with single item 50
# must include , for a single item

t = (50,)
print(t)

# Exercise 7: Unpack the tuple into 4 variables 


t = (10, 20, 30, 40)

a, b, c, d = t

print(a)
print(b)
print(c)
print(d)

# Exercise 8: Swap two tuples in Python


t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Swap tuples
t1, t2 = t2, t1

print("t1:", t1)
print("t2:", t2)


# Exercise 9: Copy Specific Elements From Tuple 

t = (10, 20, 30, 40, 50)


new_tuple = (t[1], t[3])

print(new_tuple)

# Exercise 10: List to Tuple


my_list = [10, 20, 30, 40]

# Convert list to tuple
my_tuple = tuple(my_list)

print(my_tuple)

# Exercise 11: Function Returning Tuple 


def get_values():
    return 10, 20, 30

result = get_values()

print(result)

# Unpacking returned tuple


def get_values():
    return 10, 20, 30

a, b, c = get_values()

print(a)
print(b)
print(c)

# Exercise 12: Comparing Tuples 


t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(t1 == t2)

# Exercise 13: Removing Duplicates from Tuple 


t = (1, 2, 3, 2, 4, 1)

unique_tuple = tuple(set(t))

print(unique_tuple)

# or 


t = (1, 2, 3, 2, 4, 1)

unique_list = []
for item in t:
    if item not in unique_list:
        unique_list.append(item)

unique_tuple = tuple(unique_list)

print(unique_tuple)

# Exercise 14: Filter Tuples

t = (10, 15, 20, 25, 30)

filtered = tuple(x for x in t if x % 2 == 0)

print(filtered)

# or strings


t = ("apple", "banana", "kiwi", "grape")

filtered = tuple(x for x in t if len(x) > 4)

print(filtered)

# Exercise 15: Map Tuples 


mapped = tuple(x * 2 for x in t)

print(mapped)

# Exercise 16: Modify Tuple 


t = (10, 20, 30, 40)

# Convert to list
temp = list(t)

# Modify element
temp[1] = 25

# Convert back to tuple
t = tuple(temp)

print(t)

# Exercise 17: Sort a tuple of tuples by 2nd item 

t = ((1, 3), (4, 1), (2, 2))


sorted_t = tuple(sorted(t, key=lambda x: x[1]))

print(sorted_t)

# Exercise 18: Count Elements 


t = (1, 2, 3, 2, 4, 2)

count = t.count(2)

print(count)

# using loop

t = (1, 2, 3, 2, 4, 2)

count = 0
for item in t:
    if item == 2:
        count += 1

print(count)

# Exercise 19: Check if all items in the tuple are the same

t = (5, 5, 5, 5)
is_same = len(set(t)) == 1

print(is_same)





