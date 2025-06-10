# Implement Your Own Data Structure

This project is a simple interactive **Inventory Manager** built using Python. It leverages core data structures—**dictionaries**, **tuples**, and **lists**—to manage items in an inventory with features like adding, removing, updating, displaying items, and calculating total value.

## Features

- Add new items to the inventory  
- Remove existing items  
- Update quantity or price of items  
- View all items in a clean, readable format  
- Calculate the total value of the inventory (quantity × price)  

## Data Structure Used

- `dict`: Used for storing item names as keys and `(quantity, price)` as tuple values  
- `tuple`: Stores quantity and price, ensuring immutability for item data blocks  
- `list`: Used for looping, displaying, and structuring outputs  

## Example Output

Welcome to the Inventory Manager!

Current inventory:
Item: apple, Quantity: 10, Price: $2.5
Item: banana, Quantity: 20, Price: $1.2

Adding a new item: mango

Updated inventory:
Item: apple, Quantity: 10, Price: $2.5
Item: banana, Quantity: 20, Price: $1.2
Item: mango, Quantity: 15, Price: $3.0

Total value of inventory: $90.0

## How to Run

Make sure you have Python 3 installed. Then in your terminal:

python main.py or python3 main.py