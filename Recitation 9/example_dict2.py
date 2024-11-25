
# Imagine this dictionary represents a shopping cart where keys are item categories
# and values are lists of items in those categories
shopping_cart = {
    'fruits': ['apple', 'banana'],
    'vegetables': ['carrot', 'broccoli'],
    'dairy': ['milk', 'cheese']
}

if 'apple' in shopping_cart['fruits']:
    print('Apple is in the shopping cart')
# output: Apple is in the shopping cart

# List of items to add to the shopping cart
new_items = {
    'fruits': 'orange',
    'vegetables': 'spinach',
    'meat': 'chicken'  # 'meat' category does not exist in the shopping cart
}

# Update the shopping cart with new items
for category, item in new_items.items():
    # Check if the category exists in the shopping cart
    if category in shopping_cart:
        # Append the item to the list of items in that category
        shopping_cart[category].append(item)
    else:
        # Create a new category in the shopping cart and add the item to the list of items in that category
        shopping_cart[category] = [item]

print(shopping_cart)

'''
Output: 
{   'fruits': ['apple', 'banana', 'orange'], 
    'vegetables': ['carrot', 'broccoli', 'spinach'], 
    'dairy': ['milk', 'cheese'], 
    'meat': ['chicken']
}
'''