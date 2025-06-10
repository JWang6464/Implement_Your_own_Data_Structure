"""
Assignment: Implement Your Own Data Structures
For Cognizant Externship – Python Fundamentals
Description:
This script creates a basic inventory management system using:
- Dictionary for storing inventory
- Tuples for quantity and price
- Lists for optional interaction

Jordan Wang
6/10/2025
"""

# Step 1: Create the Inventory
inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

def display_inventory():
    print("\nCurrent inventory:")
    for item, (quantity, price) in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

# Step 2: Add, Remove, and Update Items
def add_item(name, quantity, price):
    inventory[name] = (quantity, price) # adds a new item
    print(f"{name} added successfully.")

def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"{name} removed.")
    else:
        print(f"{name} not found in inventory.")

def update_item(name, quantity=None, price=None):
    if name in inventory:
        current_quantity, current_price = inventory[name]
        new_quantity = quantity if quantity is not None else current_quantity
        new_price = price if price is not None else current_price
        inventory[name] = (new_quantity, new_price)
        print(f"{name} updated.")
    else:
        print(f"{name} not found in inventory.")

def calculate_total_value():
    total = sum(quantity * price for quantity, price in inventory.values())
    return total

# Step 3: Display the Inventory
print("Welcome to the Inventory Manager!")
display_inventory()

print("\nAdding a new item: mango")
add_item("mango", 15, 3.0)

print("\nRemoving item: banana")
remove_item("banana")

print("\nUpdating apple quantity to 12 and price to 2.8")
update_item("apple", quantity=12, price=2.8)

display_inventory()

# Step 4: Bonus - Calculate Total Value
total_value = calculate_total_value()
print(f"\nTotal value of inventory: ${total_value:.2f}")
