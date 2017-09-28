"""
Create an application which manages an inventory of products.
- Create a product class which has a price, id, and quantity on hand.
- Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""
class Product:

    def __init__(self, pid, product_name, price, quantity):
        self.pid = pid
        self.price = price
        self.quantity = quantity
        self.product_name = product_name

    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
            print("Price updated successfully")
        else:
            print("Enter a price that is greater than zero.")

    def update_quantity(self, new_quantity, increase_quantity):
        if increase_quantity is True:
            self.quantity += new_quantity
        elif (self.quantity - new_quantity) >= 0:
            self.quantity-=new_quantity
        else:
            print("Cannot reduce quantity any further")

    def show_quantity(self):
        print(self.quantity)

    def show_product(self):
        print("Product id: {}, Product Name: {}, Price: {}, Quantity at hand: {}".format(self.pid, self.product_name, self.price, self.quantity))

class Inventory():
    def __init__(self, all_product=[]):
        # Product.__init__(pid)
        self.all_product = all_product

    def add_product(self, pid):
        self.all_product.append(pid)
        print("Product Successfully added")

    def remove_product(self, pid):
        if pid in self.all_product:
            self.all_product.remove(pid)
        else:
            print("Product is not in the inventory")
            # a = input("Would you love to add the product? yes or no:").lower()
            # if a == 'yes':
            #     return Inventory.add_product()
            # elif a == "no":
            #     pass

    def counter(self):
        print(len(self.all_product))

    def show_inventory(self):
        print(self.all_product)

pid = int(input("Enter Product id:"))
product_name = input("Enter product name:")
price = int(input("Enter price:"))
quantity = int(input("Enter quantity:"))

inv = Inventory()
inv.add_product(pid)
inv.show_inventory()
inv.remove_product(pid)

prod = Product(pid, product_name, price, quantity)
prod.update_price()
prod.update_quantity(pid, True)
prod.show_product()
