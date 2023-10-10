class shopping_cart:
    product_available = {'shirts': [15, 399], 'jeans': [10, 799], 'shoes': [5, 699], 'gadgets': [20, 1299]}

    def __init__(self, cname=''):
        self.cname = cname
        self.cart = {}

    def product_details(self):
        print()
        print("!!! Available Products Right Now !!!")
        print('-----------------------------------')
        for product, details in self.product_available.items():
            print(f'{product}: Quantity - {details[0]}, Price - {details[1]}')

    def cart_details(self):
        total_price = 0
        print(f'Customer Name: {self.cname}')
        print(f'Customer cart: ')
        customer_product = self.product_available.copy()
        print("!!! Products in your cart !!!")
        for product_name, cart_item in self.cart.items():
            quantity = cart_item['quantity']
            price_per_item = customer_product[product_name][1]
            total_item_price = quantity * price_per_item
            total_price += total_item_price
            print(f'{product_name}: Quantity - {quantity},  Final Price - {total_item_price}')
        print(f'Total Price: {total_price}')

    def add_details(self, product_name, quantity):
        print()
        print("***** Please Add Your Product Here *****")
        if product_name in self.product_available and quantity > 0:
            available_quantity = self.product_available[product_name][0]
            if product_name in self.cart:
                if quantity <= available_quantity - self.cart[product_name]['quantity']:
                    self.cart[product_name]['quantity'] += quantity
                    print(f'{quantity} {product_name}(s) added to the cart.')
                else:
                    print(f'Note: Only {available_quantity - self.cart[product_name]["quantity"]} {product_name}(s) left in the store. '
                          f'You can add {available_quantity - self.cart[product_name]["quantity"]} more.')
            else:
                if quantity <= available_quantity:
                    self.cart[product_name] = {'quantity': quantity, 'price': self.product_available[product_name][1]}
                    print(f'{quantity} {product_name}(s) added to the cart.')
                else:
                    print(f'Note: Only {available_quantity} {product_name}(s) left in the store. '
                          f'You can add {available_quantity} at most.')
        else:
            print('Invalid product or quantity.')

    def remove_details(self, product, quantity):
        print()
        print("***** Please Remove Your Product Here *****")
        if product_name in self.cart and quantity > 0:
            if quantity <= self.cart[product_name]['quantity']:
                self.cart[product_name]['quantity'] -= quantity
                if self.cart[product_name]['quantity'] == 0:
                    del self.cart[product_name]
                print(f'{quantity} {product_name}(s) removed from the cart.')
            else:
                print(f'Error: You can only remove up to {self.cart[product_name]["quantity"]} {product_name}(s).')
        else:
            print(f'{product_name} is not in your cart, so it cannot be removed.')

    @staticmethod
    def thanks_details():
        print()
        print("!!! Thank you for shopping here !!!")
        print("!!! Next time come with more money for more offers !!!")


clo = shopping_cart('Siva')

while True:
    print()
    print('------------------- WELCOME TO SHOP -------------------')
    print()
    print('Enter section 1 to display all items in the shop:')
    print('Enter section 2 to display your cart:')
    print('Enter section 3 to add a product to the cart:')
    print('Enter section 4 to remove a product from the cart:')
    print('Enter section 5 to exit: ')

    ch = int(input("Enter your section: "))

    if ch == 1:
        cart = shopping_cart()
        cart.product_details()
    elif ch == 2:
        if not clo.cart:
            print("Your cart is empty.")
        else:
            clo.cart_details()
    elif ch == 3:
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        clo.add_details(product_name, quantity)
    elif ch == 4:
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        clo.remove_details(product_name, quantity)
    elif ch == 5:
        shopping_c = shopping_cart()
        clo.thanks_details()
        break
    else:
        print()
        print('There is no section like that')
        print()
        print('Click the right section again in the menu')

