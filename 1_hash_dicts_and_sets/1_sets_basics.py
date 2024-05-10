"""
Hash:
Takes an input ('message') and returns a fixed-size string of bytes.
Every unique input will produce a unique output.
"""


def simple_hash(input_string):
	"""Converts any string into a hash value between 0 and 9."""
	summation = sum(ord(ch) for ch in input_string)
	return summation % 10  # We limit our hash range from 0 to 9


print(simple_hash('Hello'))  # outputs: 0
print(simple_hash('world'))  # outputs: 2

"""
Hash sets:
Uses hash functions to point directly to the location of the interaction,
Preferable when you want to prevent duplicates.
Order doesn't matter as much as quick retrieval.
Both 'in' operations will run in constant time 𝑂(1) 
regardless of the size of the set. 
"""

# Grocery list
grocery_list = set()

# Adding items
grocery_list.add('Milk')
grocery_list.add('Cheese')
grocery_list.add('Bread')

# Checking existence
print('Milk' in grocery_list)  # Outputs: True
print('Butter' in grocery_list)  # Outputs: False

# Add a new item
grocery_list.add('Butter')
print('Butter' in grocery_list)  # Outputs: True

# Try removing an item
grocery_list.remove('Bread')
print('Bread' in grocery_list)  # Outputs: False

# Clear the grocery list
grocery_list.clear()
print(grocery_list)  # Outputs: set()

# Create a new list and make a copy of it
new_list = set(['Eggs', 'Jam', 'Ham'])
copied_list = new_list.copy()

print(new_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}
print(copied_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}

# Modifying the copied list won't affect the original list
copied_list.remove('Ham')
print(new_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}
print(copied_list)  # Outputs: {'Eggs', 'Jam'}
