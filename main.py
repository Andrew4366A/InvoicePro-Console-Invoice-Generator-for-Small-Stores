from inventory import InventoryManager
from models import Invoice

def main():
    inventory = InventoryManager()
    inventory.load_products()

    while True:
        print("\n1. Add Product")
        print("2. View Products")
        print("3. Create Invoice")
        print("4. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            id = input("Product ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            inventory.add_product(id, name, price, stock)

        elif choice == "2":
            inventory.view_products()

        elif choice == "3":
            customer = input("Customer Name: ")
            invoice = Invoice(customer)

            while True:
                pid = input("Enter Product ID (or 'done'): ")
                if pid == "done":
                    break
                product = inventory.get_product(pid)
                if not product:
                    print("Product not found!")
                    continue
                try:
                    qty = int(input("Quantity: "))
                    if qty <= 0:
                        print("Quantity must be positive!")
                        continue
                except ValueError:
                    print("Invalid input!")
                    continue
                invoice.add_item(product, qty)

            invoice.print_invoice()
            invoice.save_to_file()
            print("Invoice saved successfully!")

        elif choice == "4":
            inventory.save_products()
            print("Saved successfully!")
            break

        else:
            print("Invalid choice!")



if __name__ == "__main__":
    main()
