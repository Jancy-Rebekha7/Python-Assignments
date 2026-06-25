# Exercise 1: Perform basic dictionary operations 


student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

# 1. Access values
print("Name:", student["name"])

# 2. Add a new key-value pair
student["grade"] = "A"

print(student)

# Exercise 2: Perform dictionary operations

# Update a value
student["age"] = 21
print("After update:", student)

#  Remove an item
student.pop("course")
print("After removal:", student)

# Check if key exists
if "name" in student:
    print("Name exists in dictionary")

# Get all keys and values
print("Keys:", student.keys())
print("Values:", student.values())


# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)

# Exercise 3: Dictionary from Lists 

keys = ["name", "age", "city"]
values = ["John", 25, "New York"]

# Create dictionary using zip()
result = dict(zip(keys, values))

print("Dictionary:", result)

#Exercise 4: Clear Dictionary 

result.clear()
print(result)

# Exercise 5: Merge two Python dictionaries into one 


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Merge dictionaries
merged = {**dict1, **dict2}

print("Merged dictionary:", merged)

# or using update()


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)

print("Merged dictionary:", dict1)

# Exercise 6: Count Character Frequencies

text = "hello world"

# Dictionary to store frequencies
char_count = {}

for char in text:
    if char != " ":  # skip spaces (optional)
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

print("Character frequencies:", char_count)

# Exercise 7: Access Nested Dictionary 


student = {
    "name": "John",
    "marks": {
        "math": 85,
        "science": 90,
        "english": 88
    }
}

# Access nested values
print("Math marks:", student["marks"]["math"])

# Exercise 8: Print the value of key ‘history’ from nested dict

student["marks"]["history"] = 75
print(student)

print(student["marks"]["history"])

# Exercise 9: Modify Nested Dictionary 

student["marks"]["history"] = 90

print(student)

# Exercise 10: Initialize dictionary with default values 


keys = ["x", "y", "z"]
default_value = 100

result = {}

for key in keys:
    result[key] = default_value

print(result)

# Exercise 11: Create a dictionary by extracting the keys from a given dictionary 


original_dict = {"a": 1, "b": 2, "c": 3}

new_dict = {key: None for key in original_dict.keys()}

print(new_dict)


# Exercise 12: Delete a list of keys from a dictionary 


my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

# Keys to delete
keys_to_remove = ["b", "c"]

# Delete keys
for key in keys_to_remove:
    if key in my_dict:
        del my_dict[key]

print(my_dict)

# Exercise 13: Check if a value exists in a dictionary 


my_dict = {"a": 1, "b": 2, "c": 3}

# Value to check
value_to_check = 2

# Check if value exists
if value_to_check in my_dict.values():
    print("Value exists")
else:
    print("Value not found")

# Exercise 14: Rename key of a dictionary


old_key = "name"
new_key = "full_name"

if old_key in my_dict:
    my_dict[new_key] = my_dict.pop(old_key)

print(my_dict)


# Exercise 15: Get the key of a minimum value 

my_dict = {"a": 10, "b": 5, "c": 8}

# Find key with minimum value
min_key = min(my_dict, key=my_dict.get)

print(min_key)

# Exercise 16: Change value of a key in a nested dictionary 


# Nested dictionary
data = {
    "student": {
        "name": "John",
        "age": 20,
        "marks": {
            "math": 85,
            "science": 90
        }
    }
}

# Change the value of a nested key
data["student"]["marks"]["math"] = 95

print(data)

# Exercise 17: Invert Dictionary 


original = {
    "a": 1,
    "b": 2,
    "c": 3
}

# Invert dictionary
inverted = {value: key for key, value in original.items()}

print(inverted)

# Exercise 18: Sort Dictionary by Keys 


data = {
    "b": 2,
    "a": 1,
    "c": 3
}

# Sort dictionary by keys
sorted_dict = dict(sorted(data.items()))

print(sorted_dict)

# Exercise 19: Sort Dictionary by Values


data = {
    "a": 3,
    "b": 1,
    "c": 2
}

# Sort dictionary by values
sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))

print(sorted_dict)

# Exercise 20: Check if All Values are Unique 


data = {
    "a": 1,
    "b": 2,
    "c": 3
}

# Check if all values are unique
is_unique = len(data.values()) == len(set(data.values()))

print(is_unique)


