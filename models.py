import datetime

class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock -= quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Product(data["id"], data["name"], data["price"], data["stock"])


class InvoiceItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity


class Invoice:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.tax_rate = 0.05

    def add_item(self, product, quantity):
        if product.stock < quantity:
            print("Not enough stock!")
            return
        item = InvoiceItem(product, quantity)
        self.items.append(item)
        product.update_stock(quantity)

    def calculate_total(self):
        subtotal = sum(item.total_price for item in self.items)
        tax = subtotal * self.tax_rate
        total = subtotal + tax
        return subtotal, tax, total

    def print_invoice(self):
        import datetime
        print("\n===== INVOICE =====")
        print(f"Customer: {self.customer_name}")
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)

        print(f"{'Item':<15}{'Qty':<8}{'Price':<10}{'Total':<10}")
        print("-" * 40)

        for item in self.items:
            print(f"{item.product.name:<15}{item.quantity:<8}{item.product.price:<10.2f}{item.total_price:<10.2f}")
        subtotal, tax, total = self.calculate_total()
        print("-" * 40)
        print(f"{'Subtotal:':<25}{subtotal:.2f}")
        print(f"{'Tax (5%):':<25}{tax:.2f}")
        print(f"{'Total:':<25}{total:.2f}")
        print("=" * 40)

    
    def save_to_file(self):
        import datetime
        filename = f"invoice_{self.customer_name}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        
        with open(filename, "w") as f:
            f.write("===== INVOICE =====\n")
            f.write(f"Customer: {self.customer_name}\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-" * 40 + "\n")
            
            f.write(f"{'Item':<15}{'Qty':<8}{'Price':<10}{'Total':<10}\n")
            f.write("-" * 40 + "\n")
            
            for item in self.items:
                f.write(f"{item.product.name:<15}{item.quantity:<8}{item.product.price:<10.2f}{item.total_price:<10.2f}\n")
            subtotal, tax, total = self.calculate_total()

            f.write("-" * 40 + "\n")
            f.write(f"{'Subtotal:':<25}{subtotal:.2f}\n")
            f.write(f"{'Tax (5%):':<25}{tax:.2f}\n")
            f.write(f"{'Total:':<25}{total:.2f}\n")
            f.write("=" * 40 + "\n")