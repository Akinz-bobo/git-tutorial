# Function to add a product to inventory
def add_product(inventory):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    inventory[name] = {"quantity": quantity, "price": price}
    print("Product added successfully.")

# Function to remove a product from inventory
def remove_product(inventory):
    name = input("Enter product name to remove: ")
    if name in inventory:
        del inventory[name]
        print("Product removed successfully.")
    else:
        print("Product not found in inventory.")

# Function to view current inventory
def view_inventory(inventory):
    print("Current Inventory:")
    for name, details in inventory.items():
        print(f"{name}: Quantity - {details['quantity']}, Price - ${details['price']}")

# Function to search for a product in inventory
def search_product(inventory):
    name = input("Enter product name to search: ")
    if name in inventory:
        print(f"Product found: {name}, Quantity - {inventory[name]['quantity']}, Price - ${inventory[name]['price']}")
    else:
        print("Product not found in inventory.")

# Function to update product details in inventory
def update_product(inventory):
    name = input("Enter product name to update: ")
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price per unit: "))
        inventory[name]['quantity'] = quantity
        inventory[name]['price'] = price
        print("Product details updated successfully.")
    else:
        print("Product not found in inventory.")

# Main program
def main():
    inventory = {}
    while True:
        print("welcome to jidris super market")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Inventory")
        print("4. Search Product")
        print("5. Update Product Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            remove_product(inventory)
        elif choice == "3":
            view_inventory(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            update_product(inventory)
        elif choice == "6":
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
