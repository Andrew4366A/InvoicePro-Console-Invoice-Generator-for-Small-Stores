import json
from models import Product

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, id, name, price, stock):
        self.products[id] = Product(id, name, price, stock)

    def view_products(self):
        for p in self.products.values():
            print(f"{p.id} | {p.name} | ₹{p.price} | Stock: {p.stock}")

    def save_products(self):
        with open("products.json", "w") as f:
            json.dump([p.to_dict() for p in self.products.values()], f)

    def load_products(self):
        try:
            with open("products.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
            
        for item in data:
            product = Product.from_dict(item)
            self.products[product.id] = product

    def get_product(self, id):
        return self.products.get(id)