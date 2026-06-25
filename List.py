#Exercise 1: Perform Basic List Operations
mylist = [1,2,3,4,5]
print(mylist[2])

mylist.pop()
mylist.pop(2)
mylist.append(6)
mylist.insert(2,7)
print(mylist)
mylist[1]= 100
print(mylist)


# Exercise 2: Perform List Manipulation 


# Create a list
numbers = [10, 20, 30, 40, 50]

# 1. Access elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 2. Add elements
numbers.append(60)        # Add at end
numbers.insert(2, 25)     # Insert at index 2
print("After adding:", numbers)

# 3. Remove elements
numbers.remove(30)        # Remove specific value

popped = numbers.pop()    # Remove last element
print("Removed last element:", popped)
print("After removing:", numbers)

# 4. Update elements
numbers[1] = 200
print("After update:", numbers)

# 5. List slicing
print("First 3 elements:", numbers[:3])

# 6. Length of list
print("Length:", len(numbers))

# Exercise 3: Sum and average of all numbers in a list 

mylist = [1,2,3,4,5]
sum = 0
for num in mylist:
    sum += num
    avg = sum/len(mylist)
print(sum)
print(avg)

#Exercise 4: Reverse a list 
mylist = [1,2,3,4,5]
print(mylist[::-1])

# Exercise 5: Turn every item of a list into its square 


mylist = [num**2 for num in range(1,6)]
print(mylist)

# Exercise 6: Find Maximum and Minimum 

print(max(mylist))
print(min(mylist))

# Exercise 7: Count Occurrences 

mylist = [1,1,2,2,4,2,5,6,5,6,7,7,6,4,4,4]
count = mylist.count(4)
print(count)

occurs = {}
for num in mylist:
    if num in occurs:
        occurs[num] += 1
    else:
        occurs[num] = 1
print(occurs)

# Exercise 8: Sort a list of numbers 

mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

# Exercise 9: Create a copy of a list 

newlist = mylist.copy()
print(f'copy of mylist is: {newlist}')

# Exercise 10: Combine two lists 

mylist1 = [1,2,3,4,5]
mylist2 = [100,200,300,400]
combined_list = mylist1 + mylist2
print(combined_list)

# or
comb_list = mylist1.extend(mylist2)
print(mylist1)

# Exercise 11: Remove empty strings from the list of strings

# Original list
strings = ["apple", "", "banana", "", "cherry", ""]

# Remove empty strings
filtered_list = [s for s in strings if s != ""]

print("Filtered list:", filtered_list)

# Exercise 12: Remove Duplicates from list 

unique_list = list(set(mylist1))
print(unique_list)

# Exercise 13: Remove all occurrences of a specific item from a list 

# Original list
numbers = [10, 20, 30, 20, 40, 20, 50]

# Item to remove
item_to_remove = 20

# Remove all occurrences
filtered_list = [num for num in numbers if num != item_to_remove]

print("Updated list:", filtered_list)

# Exercise 14: List Comprehension for Numbers

umbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print("Even numbers:", even_numbers)

# Exercise 15: Access Nested Lists 


# Nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access entire inner list
print("First inner list:", nested_list[0])

# Access specific element
print("Element:", nested_list[1][2])

# Exercise 16: Flatten Nested List

ested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

flattened = []

for sublist in nested_list:
    for item in sublist:
        flattened.append(item)

print("Flattened list:", flattened)

# Exercise 17: Concatenate two lists index-wise


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = []

for i in range(len(list1)):
    result.append(list1[i] + list2[i])

print(result)

# or using zip() and tuple unpacking


# Two lists
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Concatenate index-wise
result = [l1 + l2 for l1, l2 in zip(list1, list2)]

print("Result:", result)

# Exercise 18: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# Concatenate in required order
result = [x + y for x in list1 for y in list2]

print("Result:", result)

#or using loops

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = []

for x in list1:
    for y in list2:
        result.append(x + y)

print(result)

# Exercise 19: Iterate both lists simultaneously 


ist1 = [1, 2, 3]
list2 = ["a", "b", "c"]

# Iterate both lists together
for num, char in zip(list1, list2):
    print(num, char)

# Exercise 21: Add new item to list after a specified item


numbers = [10, 20, 30, 40]

# Item to insert after
target = 20
new_item = 25

# Find index and insert
index = numbers.index(target)
numbers.insert(index + 1, new_item)

print("Updated list:", numbers)

# Exercise 22: Extend nested list by adding the sublist


nested_list = [[10, 20], [30, 40], [50, 60]]

# Sublist to be added
sublist = [70, 80]

# Add sublist to nested list
nested_list.append(sublist)

print("Updated nested list:", nested_list)

# Exercise 23: Replace list’s item with new value if found


numbers = [10, 20, 30, 40, 50]

# Replace 30 with 300
old_value = 30
new_value = 300

if old_value in numbers:
    index = numbers.index(old_value)
    numbers[index] = new_value

print("Updated list:", numbers)
