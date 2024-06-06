class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def clear_cart(self):
        self.items = []

    def view_cart(self):
        return self.items

def main():
    cart = Cart()
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Clear cart")
        print("5. Exit")

        choice = input("Select an option: ")
        
        if choice == '1':
            item = input("Enter item to add: ")
            cart.add_item(item)
            print(f"Added {item} to cart.")
        elif choice == '2':
            item = input("Enter item to remove: ")
            cart.remove_item(item)
            print(f"Removed {item} from cart.")
        elif choice == '3':
            print("Cart contents:", cart.view_cart())
        elif choice == '4':
            cart.clear_cart()
            print("All items removed from cart.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
