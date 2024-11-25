# example_set.py

# Define a set of fruits
fruits = {"apple", "banana", "cherry", "date"}

# Function to check if a fruit is in the set
def check_fruit(fruit):
    if fruit in fruits:
        return f"{fruit} is in the set."
    else:
        return f"{fruit} is not in the set."

print(check_fruit("apple"))  # Output: apple is in the set.
print(check_fruit("mango"))  # Output: mango is not in the set.